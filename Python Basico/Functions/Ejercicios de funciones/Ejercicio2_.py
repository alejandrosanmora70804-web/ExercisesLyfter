#Scope local

def function():
    num1 = 5
    num2= 5
    suma = num1 + num2
    print(suma)


function()


#Scope global

num3 = 4
num4 = 4

def function2():
    num3 = 10
    suma2 = num3 + num4
    print(suma2)


function2()