# Cree una función que reciba un texto y un carácter, y retorne cuántas veces 
# aparece ese carácter en el texto

def function():
    string = input("Escribe un texto: ")
    character = input("Ingrese el caracter que desea buscar: ")
    accountant = 0
    for characters in string:
        if characters == character:
            accountant += 1
    return print(f"Se a encontrado {accountant} veces el caracter")


function()