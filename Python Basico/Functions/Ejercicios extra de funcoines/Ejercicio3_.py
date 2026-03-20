def function():
    string = input("Ingrese un string: ")
    vocals = "aeiouAEIOU"
    accountant  = 0
    for lyrics in string:
        if lyrics in vocals:
            accountant += 1
    return print(f"'{string}' contiene {accountant} vocales")

function()