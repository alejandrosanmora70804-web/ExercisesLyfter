class Animal: #parent class
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} are eating.")

    def sleep(self):
        print(f"{self.name} are sleeping.")


class Swimmer: #parent class
    def swim(self):
        print(f"{self.name} are swimming.")


class Flyer: #parent class
    def fly(self):
        print(f"{self.name} are flying.")


class Duck(Animal, Swimmer, Flyer): #child class, inherits from the parents classes
    def quack(self):
        print(f"{self.name} say: ¡Quack!")


donald = Duck("Donald")

donald.eat() #from Animal
donald.sleep() #from Animal
donald.swim() #from swimmer
donald.fly() #from flyer
donald.quack() #from duck


# Duck  inherits all three classes at once: Animal, Swimmer and Flyer
# It obtains all its methods without repeating code