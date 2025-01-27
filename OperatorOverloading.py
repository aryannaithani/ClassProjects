#Operator Overloading

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        else:
            return Point(self.x + other[0], self.y + other[1])

    def __sub__(self, other):
        if isinstance(other, Point):
            return Point(self.x - other.x, self.y - other.y)
        else:
            return Point(self.x - other[0], self.y - other[1])

    def __mul__(self, other):
        if isinstance(other, Point):
            return Point(self.x * other.x, self.y * other.y)
        else:
            return Point(self.x * other[0], self.y * other[1])

    def __gt__(self, other):
        if isinstance(other, Point):
            return self.x > other.x and self.y > other.y
        else:
            return self.x > other[0] and self.y > other[1]

    def __truediv__(self, other):
        if isinstance(other, Point):
            return Point(self.x / other.x, self.y / other.y)
        else:
            return Point(self.x / other[0], self.y / other[1])

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        else:
            return self.x == other[0] and self.y == other[1]

    def __lt__(self, other):
        if isinstance(other, Point):
            return self.x < other.x and self.y < other.y
        else:
            return self.x < other[0] and self.y < other[1]
