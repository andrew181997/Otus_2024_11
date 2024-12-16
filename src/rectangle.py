from figure import Figure


class Rectangle(Figure):
    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b
        self.validate_numeric(self.side_a, self.side_b)

    @property
    def get_area(self):
        result = self.side_a * self.side_b
        return round(result, 2)

    @property
    def get_perimeter(self):
        result = 2 * (self.side_a + self.side_b)
        return round(result, 2)
