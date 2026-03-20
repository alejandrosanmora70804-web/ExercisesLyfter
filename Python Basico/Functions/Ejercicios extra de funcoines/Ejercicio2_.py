# Cree una función que reciba una lista de palabras y un número n, y retorne una 
# nueva lista con solo las palabras que tengan más de n letras

def function():
    list_words= []
    while  len(list_words) < 4:
        word = input("Ingrese una palabra: ")
        list_words.append(word)
    number = int(input("Ingrese el número de letras mínimas en la palabra: "))
    new_list = []
    for word in list_words:
        if len(word) > number:
            new_list.append(word)

    return new_list

resultado = function()
print(resultado)