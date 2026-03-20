import random

num = int(input("Ingrese un número del 1 al 10: "))
num_random = random.randint(1, 10)
while num != num_random:
    num = int(input("Intente de nuevo: "))