

class Stop:
    next_stop = None

    def __init__(self, from_town, to_town, distance):
        self.origin = from_town
        self.destination = to_town
        self.distance = int(distance)

    def next(self, stop):
        self.next_stop = stop
        return self