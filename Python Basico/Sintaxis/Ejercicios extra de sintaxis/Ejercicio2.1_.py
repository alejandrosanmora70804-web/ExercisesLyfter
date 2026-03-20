import random

secret_num = random.randint(1, 10)
num = int(input("Adivina el número del 1 al 10: "))

while num != secret_num:
    num = int(input("Intenta de nuevo: "))

print(f"El número secreto es {secret_num}")