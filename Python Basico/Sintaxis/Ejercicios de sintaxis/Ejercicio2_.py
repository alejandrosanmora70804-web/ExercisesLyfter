name = input("Ingrese su nombre: ")
last_name = input("Ingrese su appellido: ")
years_old = int(input("Ingrese su edad: "))

if  years_old <= 4:
    print(f"{name} {last_name} es un bebé.")

elif years_old <= 11:
    print(f"{name} {last_name} es un niño.")

elif years_old <= 14:
    print(f"{name} {last_name} es un preadolescente.")

elif years_old <= 17:
    print(f"{name} {last_name} es un adolescente.")

elif years_old <= 24:
    print(f"{name} {last_name} es un adulto joven.")

elif years_old >= 25:
    print(f"{name} {last_name} es un adulto o adulto mayor.")