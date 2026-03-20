import json

with open('Pokémons.json', 'r', encoding='utf-8') as file:
    pokemon_list=json.load(file)
    for pokemon in pokemon_list:
        print(f'Name: {pokemon['name']['english']}')
        print(f'Type {pokemon['type']}')
        print(f'Level: {pokemon['level']}')
        print('-------------------------')