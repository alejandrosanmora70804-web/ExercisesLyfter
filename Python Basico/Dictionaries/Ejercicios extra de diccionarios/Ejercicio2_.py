employees = [
    {"name": "Carlos", "email": "carlos@empresa.com", "department": "Ventas"},
    {"name": "Ana", "email": "ana@empresa.com", "department": "TI"},
    {"name": "Luis", "email": "luis@empresa.com", "department": "Ventas"},
    {"name": "Sofía", "email": "sofia@empresa.com", "department": "RRHH"},
]

dep_employees = {}

for employee in employees:
    department = employee["department"]
    if department not in dep_employees:
        dep_employees[department] = []

    dep_employees[department].append(employee)

print(dep_employees)