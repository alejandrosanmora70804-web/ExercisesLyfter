class Circle:
    radius = 12

    def get_area(self):
        return 3.14 * (self.radius**2)
        

area_1 = Circle()
print(area_1.get_area())

area_2 = Circle()
area_2.radius = 25
print(area_2.get_area())