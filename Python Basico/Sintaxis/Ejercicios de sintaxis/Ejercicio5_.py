contador_de_notas = 1
cantidad_de_notas_aprobadas = 0
cantidad_de_notas_desaprobadas = 0
promedio_de_notas_aprobadas = 0
promedio_de_notas_desaprobadas = 0
promedio_de_notas_total = 0

total_de_notas = int(input("Ingrese la cantidad de notas: "))

while contador_de_notas <= total_de_notas:
    nota_actual = int(input("Ingrese la nota: "))
    contador_de_notas += 1
    if nota_actual < 70:
        cantidad_de_notas_desaprobadas += 1
        promedio_de_notas_desaprobadas += nota_actual
    else:
        cantidad_de_notas_aprobadas += 1
        promedio_de_notas_aprobadas += nota_actual
        
    promedio_de_notas_total = promedio_de_notas_total + (nota_actual / total_de_notas)

promedio_de_notas_desaprobadas /= cantidad_de_notas_desaprobadas
promedio_de_notas_aprobadas /= cantidad_de_notas_aprobadas
print(f"El estudiante tiene {cantidad_de_notas_aprobadas} notas aprobadas.")
print(f"{promedio_de_notas_aprobadas} este es el promedio de notas aprobadas.")
print(f"El estudiante tine {cantidad_de_notas_desaprobadas} notas desaprobadas.")
print(f"{promedio_de_notas_desaprobadas} este es el promedio de notas desaprobadas.")
print(f"{promedio_de_notas_total} este es el promedio total de notas.")