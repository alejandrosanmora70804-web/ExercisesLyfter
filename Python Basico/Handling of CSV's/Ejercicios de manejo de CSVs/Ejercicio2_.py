import csv

list_videogames = []

def register_videogames():
    number_videogames = int(input('¿How many video games do you want to register?: '))

    for videgames in range(number_videogames):
        print(f'\n--- Video Games {videgames+1} ---')
        name = input('Name: ')
        gender = input('Gender: ')
        developer = input('Developer: ')
        clasification = input('Clasification: ')

        games = {
            'Name': name,
            'Gender': gender,
            'Developer': developer,
            'Clasification': clasification
        }

        list_videogames.append(games)


def write_csv_file(file_path, data, headers):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            writer = csv.DictWriter(file, headers, dialect='excel-tab')
            writer.writeheader()
            writer.writerows(data)

    except Exception as e:
        print(f'An error occurred while saving the file: {e}')


register_videogames()
write_csv_file('video game information.csv', list_videogames, list_videogames[0].keys())