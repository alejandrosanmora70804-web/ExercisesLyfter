#Cree un programa que use una lista para eliminar keys de un diccionario.

list_of_keys = ["access_level", "age"]
employee = {
    "name": "john",
    "email": "john@ecrop.com",
    "access_level": 5,
    "age": 28
}

for key in list_of_keys:
    employee.pop(key, None)

print(employee)