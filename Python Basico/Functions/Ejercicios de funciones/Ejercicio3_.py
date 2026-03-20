my_list = [4, 6, 2, 29]

def sums_of_numbers(my_list):
    total = 0
    for number in my_list:
        total += number
    return total


print(sums_of_numbers(my_list))
# result = sums_of_numbers(my_list)
# print(result)