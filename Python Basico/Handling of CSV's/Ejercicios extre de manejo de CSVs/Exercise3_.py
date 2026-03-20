import csv

def main(file_path):
    genre_count = {}

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                gender = row['Gender'].strip().capitalize()
                if gender in genre_count:
                    genre_count[gender] += 1
                else:
                    genre_count[gender] = 1
        print("Genres found:")
        for gender in sorted(genre_count.keys()):
            print(f"{gender}: {genre_count[gender]}")

    except FileNotFoundError:
        print(f"Error: File not found '{file_path}'")
    except KeyError:
        print("Error: The 'gender' column was not found in the CSV file")

main('video game information.csv')