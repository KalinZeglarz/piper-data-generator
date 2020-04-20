from random import random
from typing import List, Iterable, Tuple

from generator.config.basic import triggers
from generator.event import Event


def _get_all_possible_events() -> List[tuple]:
    all_possible = []
    rooms = []
    for room in triggers:
        rooms.append(room)
        for trigger in triggers[room]:
            for event in triggers[room][trigger]:
                if type(event) is tuple:
                    all_possible.append(((trigger, event[0]), (trigger, event[1])))
                else:
                    all_possible.append((trigger, event))
    return all_possible, rooms


def _generate_events(n: int, start_time: int, events_pool: List[tuple]) -> Iterable[Tuple[Event, bool]]:
    current_time = start_time
    for _ in range(n):
        next_event = events_pool[int(random() * len(events_pool))]
        if type(next_event[0]) is tuple:
            yield Event(current_time, next_event[0][0], next_event[0][1]), False
            yield Event(current_time + int(random() * 3600), next_event[1][0], next_event[1][1]), True
        else:
            yield Event(current_time, next_event[0], next_event[1]), False
        current_time += int(random() * 3600)


def _generate_events_in_order(n: int, start_time: int, events_pool: List[tuple]) -> Iterable[Event]:
    buffer = []
    for event, scheduled in _generate_events(n, start_time, events_pool):
        if not scheduled:
            while len(buffer) > 0 and event.time > buffer[0].time:
                yield buffer.pop(0)
            yield event
        else:
            buffer.append(event)
            buffer.sort(key=lambda e: e.time)

    for event in buffer:
        yield event
