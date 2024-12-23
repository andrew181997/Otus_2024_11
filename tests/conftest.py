import pytest
import random


@pytest.fixture()
def random_figure():
    radius = random.randint(1, 101)
    side_a = random.randint(90, 101)
    side_b = random.randint(90, 101)
    side_c = random.randint(90, 101)
    yield radius, side_a, side_b, side_c
