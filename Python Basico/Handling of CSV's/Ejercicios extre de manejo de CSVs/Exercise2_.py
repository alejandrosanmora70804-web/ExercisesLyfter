import csv

def main(file_path):
    clasification_sought = input('Escribe una clasificación a buscar (example:"M"): ').upper()
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        
        try:
            next(reader)
        except Exception as ex:
            return
        
        found = False
        for row in reader:
            if len(row) >= 4:
                if row[3].strip().upper() == clasification_sought:
                    print(f"Nombre: {row[0]}")
                    print(f"Género: {row[1]}")
                    print(f"Desarrollador: {row[2]}")
                    print(f"Clasificación: {row[3]}")
                    print("-" * 20)
                    found = True
        
        if not found:
            print("No se encontraron videojuegos con esa clasificación.")


main('video game information.csv')