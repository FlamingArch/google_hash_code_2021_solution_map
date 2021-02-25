false = False
true = True


class Street:
    def __init__(self, start, end, name, duration):
        self.start = start
        self.end = end
        self.name = name
        self.duration = duration
    def __str__(self):

        return f':: [{id}] {self.start}, {self.end}, {self.name}, {self.duration} ::'


class Intersections:
    def __init__(self):
        ''
        pass


class Simulation:
    def __init__(self, duration, intersection_count, street_count, cars, point):
        self.duration = duration
        self.intersection_count = intersection_count
        self.street_count = street_count
        self.cars = cars
        self.point = point
        self.streets: [Street] = []

    def create_street(self, line: str):
        self.streets.append(Street(*line.split(" ")))

    def street_desc(self) -> str:
        for street in self.streets:
            print(f':: [{id}] {street.start}, {street.end}, {street.name}, {street.duration} ::')


firstLine = false
sim: Simulation
with open(input('Filename: > '), 'r') as stream:
    if firstLine:
        sim.create_street(stream.readline())
    else:
        sim = Simulation(*stream.readline().split(" "))