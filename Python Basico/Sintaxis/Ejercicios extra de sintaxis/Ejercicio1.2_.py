sec_time = int(input("Dame una cantidad en segundos: "))

if sec_time < 600:
    sec_missing = 600 - sec_time
    print(f"Los segundos faltantes son {sec_missing}")

elif sec_time > 600:
    print("Mayor")

else:
    print("Igual")