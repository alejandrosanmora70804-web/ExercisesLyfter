def validate_numbers(func):
    def wrapper(*args, **kwargs):
        for i, arg in enumerate(args):
            if not isinstance(arg, (int, float)):
                raise TypeError(f"The parameter #{i+1} '{arg}' is not a number (is {type(arg).__name__})")

        for name, valor in kwargs.items():
            if not  isinstance(valor, (int, float)):
                raise TypeError(f"The parameter '{name}={valor}' is not a number (is {type(valor.__name__)})")

        return func(*args, **kwargs)
    return wrapper


@validate_numbers
def addition(a, b):
    return a + b


@validate_numbers
def calculate_volume(length, width, height):
    return length * width * height


print(addition(3, 5))
print(addition(2.5, 4))
print(calculate_volume(2, 3, height=4))

print(addition("hi", 5))
print(addition(3, [1, 2]))
print(2, 3, height="four")