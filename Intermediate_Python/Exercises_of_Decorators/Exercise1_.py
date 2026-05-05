def log_perimeter_return(func):
    def wrapper(*args, **kwargs):
        print(f"Calling: {func.__name__}")
        print(f"Positional perimeters: {args}")
        print(f"Perimeters with name: {kwargs}")
        
        results = func(*args, **kwargs)

        print(f"return: {results}")
        return results
    return wrapper


@log_perimeter_return
def addition(a, b):
    return a + b


@log_perimeter_return
def greet(name, message="Hi"):
    return f"{message}, {name}!"


addition(3, 5)
print("---")
greet("Carlos", message="Good morning")