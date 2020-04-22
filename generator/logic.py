from random import random, choice
from typing import List, Iterable, Tuple

from generator.config.time import HOUR
from generator.model.event import Event
from generator.EventsManager import _EventsManager
from generator.model.user import User


def _generate_users(n: int, current_time: int, rooms: List[str]) -> List[User]:
    return [User(f'user_{i}', choice(rooms), current_time, current_time, rooms) for i in range(n)]


def _generate_events(n: int, users_n: int, start_time: int) -> Iterable[Event]:
    events = _EventsManager()
    current_time = start_time
    users = _generate_users(users_n, current_time, events.get_rooms())
    generated = 0
    while generated < n:
        for user in users:
            new_events = _generate_events_for_user(user, current_time, events)
            for event in new_events:
                yield event
            user.update(current_time)

            generated += len(new_events)
            if generated >= n:
                break

        current_time += 60


def _generate_events_for_user(user: User, current_time: int, events: _EventsManager) -> List[Tuple[Event, bool]]:
    if user.next_event_at <= current_time:
        next_event = events.generate(user.room, current_time)
        if next_event is None:
            user.next_event_at = user.change_state_at
            return []
        if type(next_event[0]) is tuple:
            start_event = Event(user.next_event_at, next_event[0][0], next_event[0][1])
            end_event = Event(user.next_event_at + int(random() * HOUR), next_event[1][0], next_event[1][1])
            events.block_event(start_event)
            events.block_event(end_event)
            return [
                (start_event, False),
                (end_event, True)
            ]
        else:
            single_event = Event(user.next_event_at, next_event[0], next_event[1])
            return [(single_event, False)]
    else:
        return []


def _generate_events_in_order(n: int, users_n: int, start_time: int) -> Iterable[Event]:
    buffer = []
    for event, scheduled in _generate_events(n, users_n, start_time):
        if not scheduled:
            while len(buffer) > 0 and event.time > buffer[0].time:
                yield buffer.pop(0)
            yield event
        else:
            buffer.append(event)
            buffer.sort(key=lambda e: e.time)

    for event in buffer:
        yield event
