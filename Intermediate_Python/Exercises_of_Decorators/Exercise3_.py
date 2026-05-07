from datetime import date

class User:
    def __init__(self, name, date_of_birth):
        self.name = name
        self.date_of_birth = date_of_birth

    @property
    def age(self):
        today = date.today()
        years = today.year - self.date_of_birth.year
        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            years -= 1
        return years

def __repr__(self):
    return f"User(name ={self.name}, age={self.age}"


def verify_of_legal_age(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, User) and arg.age < 18:
                raise PermissionError(f"Access denied: {arg.name} is {arg.age} years old and is a minor.")

        for key, value in kwargs.items():
            if isinstance(value, User) and value.age < 18:
                raise PermissionError(f"Access denied: {value.name} is {value.age} years old and is a minor")

        return func(*args, **kwargs)
    return wrapper

@verify_of_legal_age
def access_site(user):
    return f"Welcome, {user.name}! Access granted."

@verify_of_legal_age
def purchase_product(user, product):
    return f"{user.name} purchased: {product}."


adult = User("Carlos", date(1990, 3, 15))
minor = User("Maria", date(2012, 8, 22))

print(access_site(adult))
print(purchase_product(adult, "Laptop"))

# access_site(minor)
# purchase_product(user=minor, product="Video game")