class Rectangle:
    def __init__(self, width, height):
        if width < 0 or height < 0:
            raise ValueError("Width and height cannot be negative.")
        self.width = width
        self.height = height
    
    def get_area(self):
        return self.height * self.width
    

    def get_perimeter(self):
        return 2 * (self.height + self.width)


try:
    height = int(input("Enter the height: "))
    width = int(input("Enter the width: "))
    rectangle_1 = Rectangle(width, height)
    print(rectangle_1.get_area())
    print(rectangle_1.get_perimeter())
except ValueError as error:
    print(f"Error: {error}")

try:
    height = int(input("\nEnter the height: "))
    width = int(input("Enter the width: "))
    rectangle_2 = Rectangle(width, height)
    print(rectangle_2.get_area())
    print(rectangle_2.get_perimeter())
except ValueError as error:
    print(f"Error: {error}")
