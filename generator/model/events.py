from random import random
from typing import List, Dict
from generator.config.basic import triggers
from generator.model.event import Event


class Events:
    def __init__(self):
        self.events: Dict[str, List[any]] = self._get_all_possible_events()
        self.current_events: List[Event] = []

    def __hash__(self):
        return hash(self.events)

    def block_event(self, event: Event):
        self.current_events.append(event)

    def release_event(self, event: Event):
        self.current_events.remove(event)

    def update_blocked(self, current_time: int):
        for _ in self.current_events:
            if _.time < current_time:
                self.release_event(_)

    def get_events_keys(self) -> List[str]:
        return list(self.events.keys())

    @staticmethod
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

    def generate(self, room: str, current_time: int) -> Event:
        self.update_blocked(current_time)
        events_pool = self.events[room]
        while True:
            is_free: bool = True
            next_event: Event = events_pool[int(random() * len(events_pool))]
            if type(next_event) is tuple:
                for _ in self.current_events:
                    if next_event[0][0] == _.trigger and next_event[0][1] == _.name:
                        is_free = False
                        break
            if is_free:
                break
        return next_event
