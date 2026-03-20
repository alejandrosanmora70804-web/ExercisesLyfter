price = int(input("¿Cuál es el preccio del producto?: "))

if price < 100:
    discount = price * 0.02
else:
    discount = price * 0.10

final_price = price - discount
print(f"El precio final es {final_price}")