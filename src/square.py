from rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, side_a):
        self.side_a = side_a
        super(Square, self).__init__(side_a, side_a)
        self.validate_numeric(self.side_a, self.side_a)
