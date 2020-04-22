from typing import List, Dict, Set
from generator.config.basic import triggers
from generator.model.event import Event


class Events:
    def __init__(self):
        self.events: Dict[str, List[any]] = self._get_all_possible_events()
        self.current_events: Set[Event] = set()

    def __hash__(self):
        return hash(self.events)

    def block_event(self, event: Event):
        self.current_events.add(event)

    def release_event(self, event: Event):
        self.current_events.remove(event)

    def update_blocked(self, current_time: int):
        to_remove = []
        for e in self.current_events:
            if e.time < current_time:
                to_remove.append(e)

        for e in to_remove:
            self.release_event(e)

    @staticmethod
    def get_rooms() -> List[str]:
        return list(triggers.keys())

    @staticmethod
    def _get_all_possible_events() -> Dict[str, List[any]]:
        all_possible: Dict[str, List[any]] = {}
        for room in triggers:
            all_possible[room] = []
            for trigger in triggers[room]:
                for event in triggers[room][trigger]:
                    if type(event) is tuple:
                        all_possible[room].append(((trigger, event[0]), (trigger, event[1])))
                    else:
                        all_possible[room].append((trigger, event))
        return all_possible

    def generate(self, room: str, current_time: int) -> any:
        self.update_blocked(current_time)
        events_pool = self.events[room]
        for next_event in events_pool:
            if type(next_event) is tuple:
                if next_event[1] not in set(map(lambda e: (e.trigger, e.name), self.current_events)):
                    return next_event
        return None
