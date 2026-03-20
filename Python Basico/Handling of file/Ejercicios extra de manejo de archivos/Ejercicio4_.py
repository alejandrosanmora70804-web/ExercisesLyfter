new_line = input('Introduce el texto que deseas guardar: ')

with open('File4.txt', 'a', encoding='utf-8') as file:
    file.write(new_line + '\n')