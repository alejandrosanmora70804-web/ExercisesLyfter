#Cree un programa que reciba una lista de números y calcule el promedio de los valores, luego cree una nueva lista con solo 
#los valores mayores al promedio

my_list = [10, 20, 30, 40, 50]
new_list = []
suma= 0

for n in my_list:
    suma += n
    average = suma / len(my_list)

for n in my_list:
    if n > average:
        mayor = n
        new_list.append(mayor)

print(f"Promedio: {average}")
print(new_list)