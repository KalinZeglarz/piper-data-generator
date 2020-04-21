from random import random, choice
from typing import List, Iterable, Tuple, Dict

from generator.config.basic import triggers
from generator.config.time import HOUR
from generator.model.event import Event
from generator.model.user import User


def _get_all_possible_events() -> Dict[str, List[any]]:
    all_possible: Dict[str, List[any]] = {}
    for room in triggers:
        for trigger in triggers[room]:
            all_possible[trigger] = []
            for event in triggers[room][trigger]:
                if type(event) is tuple:
                    all_possible[trigger].append(((trigger, event[0]), (trigger, event[1])))
                else:
                    all_possible[trigger].append((trigger, event))

    return all_possible


def _generate_users(n: int, current_time: int, rooms: List[str]) -> List[User]:
    return [User(f'user_{i}', choice(rooms), current_time, current_time, rooms) for i in range(n)]


def _generate_events_for_user(user: User, current_time: int, events_pool: List[tuple]) -> List[Tuple[Event, bool]]:
    if user.next_event_at <= current_time:
        next_event = events_pool[int(random() * len(events_pool))]
        if type(next_event[0]) is tuple:
            return [
                (Event(user.next_event_at, next_event[0][0], next_event[0][1]), False),
                (Event(user.next_event_at + int(random() * HOUR), next_event[1][0], next_event[1][1]), True)
            ]
        else:
            return [(Event(user.next_event_at, next_event[0], next_event[1]), False)]
    else:
        return []


def _generate_events(n: int, users_n: int, start_time: int, events_pool: Dict[str, List[any]]) -> Iterable[Tuple[Event, bool]]:
    current_time = start_time
    users = _generate_users(users_n, current_time, list(events_pool.keys()))
    generated = 0
    while generated < n:
        for user in users:
            new_events = _generate_events_for_user(user, current_time, events_pool[user.room])
            for event in new_events:
                yield event
            user.update(current_time)

            generated += len(new_events)
            if generated >= n:
                break

        current_time += 60


def _generate_events_in_order(n: int, users_n: int, start_time: int, events_pool: Dict[str, List[any]]) -> Iterable[Event]:
    buffer = []
    for event, scheduled in _generate_events(n, users_n, start_time, events_pool):
        if not scheduled:
            while len(buffer) > 0 and event.time > buffer[0].time:
                yield buffer.pop(0)
            yield event
        else:
            buffer.append(event)
            buffer.sort(key=lambda e: e.time)

    for event in buffer:
        yield event
