class Person:
    def __init__(self, name):
        self.name = name


class Bus:
    def __init__(self, max_passengers):
        self.max_passengers = max_passengers
        self.passengers = []


    def add_passenger(self, person):
        if len(self.passengers) < self.max_passengers:
            self.passengers.append(person)
            print(f"{person.name} boarded the bus.")
        else:
            print("The bus is full, no more passengers can get on.")


    def remove_passenger(self, person):
        if person in self.passengers:
            self.passengers.remove(person)
            print(f"{person.name} got off the bus.")
        else:
            print(f"{person.name} is not on the bus.")


person1 = Person("Alejandro")
person2 = Person("María")
person3 = Person("Juan")
person4 = Person("Ana")
person5 = Person("Pedro")

bus = Bus(4)

bus.add_passenger(person1)
bus.add_passenger(person5)
bus.add_passenger(person2)
bus.add_passenger(person4)
bus.add_passenger(person3)
print()

bus.remove_passenger(person5)
bus.remove_passenger(person3)
bus.remove_passenger(person1)
bus.remove_passenger(person4)
bus.remove_passenger(person2)