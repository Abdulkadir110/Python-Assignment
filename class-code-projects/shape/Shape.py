
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
        return self._length * self._breadth

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self._radius = radius

    def get_area(self):
        return 3.142 * self._radius * self._radius
