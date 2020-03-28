from time import time
from typing import Iterable

from generator.event import Event
from generator.logic import _get_all_possible_events, _generate_events_in_order


def generate_events(n: int, start_time: int = int(time())) -> Iterable[Event]:
    events_pool = _get_all_possible_events()
    return _generate_events_in_order(n, start_time, events_pool)