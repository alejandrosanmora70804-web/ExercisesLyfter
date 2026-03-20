#Cree un programa que le pida al usuario ingresar 5 palabras. Luego muestre una nueva lista con solo aquellas palabras que 
#tengan más de 4 letras

my_list = []
new_list = []

accountaint = 0
while accountaint < 5:
    word = input("Ingrese una plabra: ")
    my_list.append(word)
    accountaint += 1

for word in my_list:
    if len(word) > 4:
        new_list.append(word)

print(my_list)
print(new_list)