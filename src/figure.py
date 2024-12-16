from abc import ABC, abstractmethod


class Figure(ABC):
    @property
    @abstractmethod
    def get_perimeter(self):
        pass

    @property
    @abstractmethod
    def get_area(self):
        pass
    @staticmethod
    def validate_numeric(*args):
        """Метод для проверки, что параметры являются валидными."""
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise ValueError(
                    f"Invalid value {arg}: All parameters must be numeric!"
                )
            if arg <= 0:
                raise ValueError(
                    f"Invalid value {arg}: All parameters must be greater than zero!"
                )

    def add_area(self, figure):
        if not isinstance(figure, Figure):
            raise ValueError("A non-geometric shape has been passed")
        return self.get_area + figure.get_area
