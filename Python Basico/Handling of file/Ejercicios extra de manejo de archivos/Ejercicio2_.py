with open('File2.txt', 'r', encoding='utf-8') as file:
    content = file.read()

    list_of_words = content.split()

    total_words = len(list_of_words)

print(f'Este archivo contiene {total_words} palabras')