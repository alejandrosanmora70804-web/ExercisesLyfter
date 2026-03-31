class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


class Inventory:
    def __init__(self):
        self.product_list = []

    
    def add_product(self, product):
        self.product_list.append(product)


    def view_products(self):
        for product in self.product_list:
            print(product.name)
            print(product.price)
            print(product.quantity)
            print("-"*10)


    def calculate_total_price(self):
        total_price = 0

        for product in self.product_list:
            total_price += product.price * product.quantity

        return f"total price: {total_price}"


product1 = Product("Mouse", 5000, 3)
product2 = Product("Teclado", 8000, 2)

inventory = Inventory()
inventory.add_product(product1)
inventory.add_product(product2)

inventory.view_products()
print(inventory.calculate_total_price())