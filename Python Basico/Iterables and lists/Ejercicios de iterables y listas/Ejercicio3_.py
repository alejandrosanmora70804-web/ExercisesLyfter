my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

temporal = my_list[0]
my_list[0] = my_list[-1]
my_list[-1] = temporal

print(my_list)