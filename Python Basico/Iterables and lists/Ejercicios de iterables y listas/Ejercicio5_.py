num_list = []
contador = 0
mayor = 0

while contador < 10:
    num = int(input("Ingrese un número: "))
    num_list.append(num)
    if num > mayor:
        mayor = num
    contador += 1

print(f"{num_list}. El más alto fue {mayor}.")