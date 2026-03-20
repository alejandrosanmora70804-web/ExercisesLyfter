#Cree un programa que cree un diccionario usando dos listas del mismo tamaño, usando una para sus keys, y la otra para sus 
# values.

list_a = ["first_name", "last_name", "role"]
list_b = ["Alejandro", "Sánchez", "Software Engineer"]
dictionary = {}

for i in range(0, len(list_a)):
    dictionary[list_a[i]] = list_b[i]

print(dictionary)