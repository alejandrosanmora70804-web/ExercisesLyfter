my_list = ['10', 'manzana', '5.5', '3', 'n/a']

def addition(my_list):
    addition_float = 0
    for element in my_list:
        try:
            float_element = float(element)
            addition_float += float_element
            print(f'{float_element} sumado correctamente')
        except ValueError:
            print(f'Elemento inválido: {element}')

    print(f'Total de la suma: {addition_float}')


addition(my_list)