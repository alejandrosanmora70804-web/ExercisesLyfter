def addition(current_number):
    print("Elegiste la opción de summa!")
    accountant = 0

    while accountant == 0:
        try:
            print("Ingrese el número que desea sumar!")
            addition_num = float(input(f"{current_number} + "))
            result = current_number + addition_num
            print(f"= {result}")
            accountant += 1
        except ValueError:
            print("El número a sumar NO puede ser una letra!")
            print()

    return result


def subtraction(current_number):
    print("Elegiste la opción de resta!")
    accountant = 0

    while accountant == 0:
        try:
            print("Ingrese el número que desea restar!")
            subtraction_num = float(input(f"{current_number} - "))
            result = current_number - subtraction_num
            print(f"= {result}")
            accountant += 1
        except ValueError:
            print("El número a restar NO puede ser una letra!")
            print()

    return result


def multiplication(current_number):
    print("Elegiste la opción de multiplicar!")
    accountant = 0

    while accountant == 0:
        try:
            print("Ingrese el número que desea multiplicar!")
            multiplication_num = float(input(f"{current_number} * "))
            result = current_number * multiplication_num
            print(f"= {result}")
            accountant += 1
        except ValueError:
            print("El número a multiplicar NO puede ser una letra")
            print()

    return result


def divition(current_number):
    print("Elegiste la opción de dividir!")
    accountant = 0

    while accountant == 0:
        try:
            print("Ingresa el númmero que deseas dividir!")
            divition_num = float(input(f"{current_number} / "))
            result = current_number / divition_num
            print(f"= {result}")
            accountant += 1
        except ValueError:
            print("El número a dividir NO puede ser una letra!")
            print()
        except ZeroDivisionError:
            print("El número a dividir NO puede ser 0!")
            print()

    return result


def delete_result(current_number):
    current_number = 0
    print("Se ha Borrado el resultdo(número actual)!")
    accountant = 0

    while accountant == 0:
        try:
            current_number = float(input("Ingrese el nuevo número actual: "))
            accountant += 1
        except ValueError:
            print("El número actul no puede ser una letra!")
            print()
    
    return current_number


def main():
    print("CALCULADORA")
    accontant = 0

    while accontant == 0:
        try:
            current_number = float(input("Ingrese el número actual: "))
            print()
            accontant += 1
        except ValueError:
            print("El número actul no puede ser una letra!")
            print()

    option = 0
    while option != 6:
        try:
            print("1. Suma")
            print("2. Resta")
            print("3. Multiplicación")
            print("4. División")
            print("5. Borrar resultado")
            option = int(input("Ingrese el número de la opción que quiere realizar: "))
            print()
        except ValueError:
            print("Tienes que elegir una de las opciones que aparcen en pantalla!")
            print()

        if option == 1:
            current_number = addition(current_number)
            input("Presione ENTER para volver: ")
            print()
        elif option == 2:
            current_number = subtraction(current_number)
            input("Presione ENTER para volver: ")
            print()
        elif option == 3:
            current_number = multiplication(current_number)
            input("Presione ENTER para volver: ")
            print()
        elif option == 4:
            current_number = divition(current_number)
            input("Presione ENTER para volver: ")
            print()
        elif option == 5:
            current_number = delete_result(current_number)
            print("Presione ENTER para volver: ")
            print()


main()