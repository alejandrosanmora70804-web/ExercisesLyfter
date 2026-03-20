#Cree un programa que muestre el valor más pequeño de una lista sin usar min().

my_list = [9, 4, 7, 1, 5]
num_min = my_list[0]

for n in my_list:
    if n < num_min:
        num_min = n
    else:
        continue

print(f"El menor valor es {num_min}")