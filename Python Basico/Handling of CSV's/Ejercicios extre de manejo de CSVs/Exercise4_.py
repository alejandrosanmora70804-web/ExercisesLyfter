import csv

def filter_by_developer(file_path):
    target_dev = input("Enter the developer name (e.g., Ubisoft): ").strip()
    games_found = []

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                if row['Developer'].strip().lower() == target_dev.lower():
                    games_found.append(row)

        if games_found:
            print(f"\nVideo games developed by {target_dev}:")
            for game in games_found:
                print(f"- {game['Name']} (Classification: {game['Clasification']}, Genre: {game['Gender']})")
        else:
            print(f"\nNo games found for developer: {target_dev}")

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except KeyError as e:
        print(f"Error: Missing column in CSV: {e}")


filter_by_developer('video game information.csv')