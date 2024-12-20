import pytest
from src.figure import Figure
from src.circle import Circle, NUM_P
from src.triangle import Triangle
from src.rectangle import Rectangle
from src.square import Square


def test_add_area_r_c(random_figure):
    "Тест проверяющий сложение площадей прямоугольника и круга"
    radius, side_a, side_b, _ = random_figure
    circle = Circle(radius)
    rectangle = Rectangle(side_a,side_b)
    expected_area = round((rectangle.get_area) + (circle.get_area), 2)
    result = circle.add_area(rectangle)
    assert  expected_area == result, f"Expected {expected_area}, got {result}"

def test_add_area_s_t(random_figure):
    "Тест проверяющий сложение площадей квадрата и треугольника"
    radius, side_a, side_b, side_c = random_figure
    square = Square(radius)
    triangle = Triangle(side_a, side_b, side_c)

    expected_area = round((square.get_area) + (triangle.get_area), 2)
    result = square.add_area(triangle)
    assert  expected_area == result, f"Expected {expected_area}, got {result}"