with open('File1.txt', 'r', encoding='utf-8') as file, open('File3.txt', 'w', encoding='utf-8') as new_file:
    for line in file:
        capital_letter_line = line.upper()

        new_file.write(capital_letter_line)