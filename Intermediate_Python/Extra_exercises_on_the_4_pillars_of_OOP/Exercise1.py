class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary

    @property
    def name(self):
        print("Reading name...")
        return self._name
    
    @name.setter
    def name(self, value):
        self._name =  value

    @property
    def salary(self):
        print("Reading salary...")
        return self._salary
    
    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("The salary can't be negative.")
        self._salary = value

    def promote(self, percentage):
        self.salary = self._salary * (1 + percentage)


employee = Employee("Ana", 1000)
print(employee.name)
print(employee.salary)

employee.promote(0.1)
print(employee.salary)