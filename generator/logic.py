from random import random
from typing import List, Iterable, Tuple

from generator.event import Event
from generator.AvailableEvents import AvailableEvents


def _generate_events(n: int, start_time: int) -> Iterable[Tuple[Event, bool]]:
    available_events = AvailableEvents()
    current_time = start_time
    for _ in range(n):
        next_event = available_events.generate()
        if type(next_event[0]) is tuple:
            yield Event(current_time, next_event[0][0], next_event[0][1]), False
            second_event = Event(current_time + int(random() * 3600), next_event[1][0], next_event[1][1])
            available_events.change_second(second_event)
            yield second_event, True
        else:
            yield Event(current_time, next_event[0], next_event[1]), False
        current_time += int(random() * 3600)


def _generate_events_in_order(n: int, start_time: int) -> Iterable[Event]:
    buffer = []
    for event, scheduled in _generate_events(n, start_time):
        if not scheduled:
            while len(buffer) > 0 and event.time > buffer[0].time:
                yield buffer.pop(0)
            yield event
        else:
            buffer.append(event)
            buffer.sort(key=lambda e: e.time)

    for event in buffer:
        yield event
