class Event:
    def __init__(self, time, trigger, name):
        self.time = time
        self.trigger = trigger
        self.name = name

    def __str__(self):
        return f'Event(time={self.time}, trigger={self.trigger}, name={self.name})'

    def __hash__(self):
        return hash((self.trigger, self.name))

    def is_same(self, other: any):
        assert type(other) is Event
        return self.trigger == other.trigger and self.name == other.name
