from random import random

from generator.config.basic import triggers


class AvailableEvents:
    def __init__(self):
        all_possible = []
        for trigger in triggers:
            for event in triggers[trigger]:
                if type(event) is tuple:
                    all_possible.append(((trigger, event[0]), (trigger, event[1])))
                else:
                    all_possible.append((trigger, event))

        self.events = all_possible
        self.first_event = None
        self.second_event = None

    def __hash__(self):
        return hash(self.events)

    def change_last(self, event):
        self.second_event = event

    def generate(self):
        if self.first_event is not None:
            while True:
                next_event = self.events[int(random() * len(self.events))]
                if next_event[0] is 'temp_up' or 'temp_down':
                    break
                elif next_event is not self.first_event and not self.second_event:
                    for i in next_event:
                        if next_event[i][0] is not self.first_event[i][0] \
                                and self.first_event[i][1] \
                                and self.second_event[i][0] \
                                and self.second_event[i][0]:
                            break
        else:
            next_event = self.events[int(random() * len(self.events))]
        self.first_event = next_event
        return next_event
