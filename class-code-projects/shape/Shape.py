
class Shape:
    def __init__(self,color):
        self._color = color

    def get_area(self):
        pass


class Rectangle(Shape):
    def __init__(self, color, length, breadth):
        super().__init__(color)
        self._length = length
        self._breadth = breadth

    def get_area(self):
        return round(self._length * self._breadth, 2)

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self._radius = radius

    def get_area(self):
        return round((22/7) * (self._radius * self._radius), 2)
