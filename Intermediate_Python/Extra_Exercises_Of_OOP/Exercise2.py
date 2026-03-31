class Animal:
    def __init__(self, name):
        self.name = name

    
    def speak(self):
        return "Makes a sound"

class Dog(Animal):
    def speak(self):
        return "Guau"


class Cat(Animal):
    def speak(self):
        return "Miau"


dog = Dog("Firulais")
print(dog.speak())

cat = Cat("Michi")
print(cat.speak())