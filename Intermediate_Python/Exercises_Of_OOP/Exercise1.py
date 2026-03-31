class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return 3.14 * (self.radius**2)
        

area_1 = Circle(12)
print(area_1.get_area())

area_2 = Circle(25)
print(area_2.get_area())