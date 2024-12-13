from math import sqrt
from figure import Figure

NUM_P = 3.14159


class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius
        super(Circle, self).__init__()
        self.validate_numeric(self.radius)

    @property
    def get_area(self):
        result = NUM_P * sqrt(self.radius)
        return round(result, 2)

    @property
    def get_perimeter(self):
        result = 2 * self.radius * NUM_P
        return round(result, 2)
