numbers_list = [1, 4, 6, 7, 13, 9, 67]

def prime_numbers1(n):
    if n <= 1:
        return False
    
    for num in range(2, int(n ** 0.5) + 1):
        if n % num == 0:
            return False
    
    return True


def prime_numbers2(numbers_list):
    prime_numbers = []
    for number in numbers_list:
        if prime_numbers1(number):
            prime_numbers.append(number)

    return prime_numbers


print(prime_numbers2(numbers_list))