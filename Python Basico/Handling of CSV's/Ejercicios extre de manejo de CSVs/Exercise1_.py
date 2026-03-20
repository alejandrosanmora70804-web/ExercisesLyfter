import csv

def main(file_path, ):
    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.reader(file)

        next(reader)

        for row in reader:
            if row and len(row) >= 4:
                print(f"Nombre: {row[0]}")
                print(f"Género: {row[1]}")
                print(f"Desarrollador: {row[2]}")
                print(f"Clasificación: {row[3]}")
                print('-' * 20)


main('video game information.csv')