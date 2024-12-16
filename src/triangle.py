from figure import Figure
from math import sqrt


class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        self.validate_numeric(self.side_a, self.side_b, self.side_c)
        if not (
            self.side_a + self.side_b > self.side_c
            and self.side_a + self.side_c > self.side_b
            and self.side_c + self.side_b > self.side_a
        ):
            raise ValueError("Triangle cannot be created")

    @property
    def get_area(self):
        p = (self.side_a + self.side_b + self.side_c) / 2
        result = sqrt(p * (p - self.side_a) * (p - self.side_b) * (p - self.side_c))
        return round(result, 2)

    @property
    def get_perimeter(self):
        return self.side_a + self.side_b + self.side_c


