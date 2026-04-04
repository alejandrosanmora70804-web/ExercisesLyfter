from abc import ABC, abstractmethod

class Shape(ABC): # parent class and child class from ABS
    @abstractmethod
    def calculate_perimeter(self):
        pass

    @abstractmethod
    def calculate_area(self):
        pass


class Circle(Shape): # child class
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    def calculate_perimeter(self):
        return 2 * self.pi * self.radius
    
    def calculate_area(self):
        return self.pi *self.radius ** 2
    

class Square(Shape): # child class
    def __init__(self, side):
        self.side = side

    def calculate_perimeter(self):
        return 4 * self.side

    def calculate_area(self):
        return self.side ** 2

class Rectangle(Shape): # child class
    def __init__(self, width, height):
        self.width = width
        self.height =  height

    def calculate_perimeter(self):
        return 2 * (self.width  + self.height)
    
    def calculate_area(self):
        return self.width * self.height


circle = Circle(5)
square = Square(4)
rectangle = Rectangle(6, 3)

print("=== Circle (radius=5) ===")
print(f"  Area:      {circle.calculate_area()}")
print(f"  Perimeter: {circle.calculate_perimeter()}")

print("=== Square (side=4) ===")
print(f"  Area:      {square.calculate_area()}")
print(f"  Perimeter: {square.calculate_perimeter()}")

print("=== Rectangle (width=6, height=3) ===")
print(f"  Area:      {rectangle.calculate_area()}")
print(f"  Perimeter: {rectangle.calculate_perimeter()}")