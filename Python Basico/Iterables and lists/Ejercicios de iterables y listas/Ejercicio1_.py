first_list = ["Hay", "en", "que", "iteracion", "indices", "muy"]
second_list = ["casos", "los", "la", "por", "es", "util"]

for index in range(0, len(first_list), len(second_list)):
    index = 0
    while index < len(first_list) and len(second_list):
        print(first_list[index], second_list[index])
        index += 1