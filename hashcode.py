false = False
true = True

class Graph(object):

    # Initialize the matrix
    def __init__(self, size):
        self.adjMatrix = []
        for i in range(size):
            self.adjMatrix.append([0 for i in range(size)])
        self.size = size

    # Add edges
    def add_edge(self, v1, v2):
        if v1 == v2:
            print("Same vertex %d and %d" % (v1, v2))
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1

    # Remove edges
    def remove_edge(self, v1, v2):
        if self.adjMatrix[v1][v2] == 0:
            print("No edge between %d and %d" % (v1, v2))
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0

    def __len__(self):
        return self.size

    # Print the matrix
    def print_matrix(self):
        for row in self.adjMatrix:
            for val in row:
                print('{:4}'.format(val)),
            print


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

for var in sim.streets:
    print(var.name)