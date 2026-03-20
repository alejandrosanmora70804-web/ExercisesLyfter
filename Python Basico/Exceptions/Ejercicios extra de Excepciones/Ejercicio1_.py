accountant = 0

while accountant == 0:
    try:
        name = input("Ingrese su nombre: ")
        if name.isdigit():
            raise ValueError("El nombre no puede ser un número!")
        accountant += 1

        while accountant == 1:
            try:
                age = int(input("Ingrese su edad: "))
                accountant += 1
                print(f"Hola {name}, su edad es {age}")
            except ValueError:
                print("Número no valido!")
                print()

    except ValueError as error:
        print(error)
        print()