with open('File1.txt', 'r', encoding='utf-8') as original_file, open('File2.txt', 'w', encoding='utf-8') as new_file:
    
    clean_content = []

    for line in original_file:
        word = line.strip()
        if word:
            clean_content.append(word)

    result = ' '.join(clean_content)
    new_file.write(result)