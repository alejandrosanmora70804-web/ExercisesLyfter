import json

# Read the Pokémon JSON file
with open("Pokémons.json", "r", encoding="utf-8") as file:
    pokemons = json.load(file)

groups = {}

for pokemon in pokemons:
    for pokemon_type in pokemon["type"]:
        if pokemon_type not in groups:
            groups[pokemon_type] = []
        groups[pokemon_type].append(pokemon["level"])

for pokemon_type, levels in groups.items():
    average = sum(levels) / len(levels)
    print(f"Type: {pokemon_type} -> Average level: {average}")