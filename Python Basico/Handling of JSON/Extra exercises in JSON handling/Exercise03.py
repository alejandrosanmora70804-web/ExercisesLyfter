import json

with open("Pokémons.json", "r", encoding="utf-8") as file:
    pokemons = json.load(file)

for pokemon in pokemons:
    print(f"Name:    {pokemon['name']['english']}")
    print(f"Attack:  {pokemon['base']['Attack']}")
    print(f"Defense: {pokemon['base']['Defense']}")
    print(f"Speed:   {pokemon['base']['Speed']}")
    print()