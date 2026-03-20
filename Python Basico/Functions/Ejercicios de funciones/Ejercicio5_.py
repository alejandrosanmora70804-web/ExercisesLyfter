def print_numbers(string):
    capital = 0
    minuscule = 0 
    for lyrics in string:
        if lyrics.isupper():
            capital += 1
        elif lyrics.islower():
            minuscule += 1

    print(f"There's {capital} upperr cases and {minuscule} lower cases")


print_numbers("I love Nación Sushi")

# .isupper() --> selecciona las letras mayúsculas
# .islower() --> selecciona las letras minúsculas