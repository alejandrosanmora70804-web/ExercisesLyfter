#Cree un programa que cuente cuántas veces aparece un número específico en una lista. 
#Pida al usuario una lista de números y otro número a buscar

my_list = []
num_look_for = 0
accountant = 0
accountant2 = 0

while accountant < 10:
    my_list.append(int(input("Ingrese un número: ")))
    accountant += 1

num_look_for = int(input("Ingrese un número a buscar: "))

for n in my_list:
    if num_look_for == n:
        accountant2 += 1

print(f"El número {num_look_for} aparece {accountant2} veces.")