my_list = ["4", "hola", "10", "5.2"]

def convert_integer (my_list):
    print('resultado:')
    for element in my_list:
        try:
            integer_element = int(element)
            print(f'"{element}" convertido a {integer_element}')
        except ValueError:
            print(f'No se puede convertir el elemento: "{element}"')


convert_integer(my_list)