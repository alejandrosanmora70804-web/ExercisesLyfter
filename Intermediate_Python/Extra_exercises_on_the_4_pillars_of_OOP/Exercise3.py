from abc import ABC, abstractmethod

class Vehicle:
    def __init__(self, brand, year):
        self._brand = brand
        self._year = year

    @abstractmethod
    def get_info(self):
        pass

class Car(Vehicle):
    def __init__(self, brand, year, doors):
        super().__init__(brand, year)
        self.doors = doors

    def get_info(self):
        return f"{self._brand} ({self._year}) - {self.doors} doors."

class Motorcycle(Vehicle):
    def __init__(self, brand, year, type):
        super().__init__(brand, year)
        self.type = type

    def get_info(self):
        return f"{self._brand} ({self._year}) - type: {self.type}."

vehicle1 = Car("Toyota", 2020, 4)
vehicle2 = Motorcycle("Yamaha", 2022, "Sports")


print(vehicle1.get_info())
print(vehicle2.get_info())