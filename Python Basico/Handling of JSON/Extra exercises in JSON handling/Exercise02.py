import json

with open('Pokémons.json', 'r', encoding='utf-8') as file:
    pokemon_list=json.load(file)

    type_pokemon=input('Enter a type of Pokemon(Water, Electric, Fire, etc): ')

    for pokemon in pokemon_list:
        if pokemon['type']==type_pokemon:
            print('The pokemons that exist of that type are:')
            print(pokemon['name']['english'])