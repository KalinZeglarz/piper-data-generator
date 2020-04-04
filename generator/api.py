from time import time
from typing import Iterable

from generator.event import Event
from generator.logic import _generate_events_in_order


def generate_events(n: int, start_time: int = int(time())) -> Iterable[Event]:
    return _generate_events_in_order(n, start_time)