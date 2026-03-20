import json

def add_pokemon():
    file_name = 'Pokémons.json'

    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            list_pokemon = json.load(file)
    except FileNotFoundError:
        list_pokemon = []

    print("--- Registration of New Pokémon ---")
    name = input("Name: ")
    level = int(input("Level: "))
    type_ = input("Type (if there is more than one, separate them with a comma): ").split(',')
    
    type_ = [t.strip() for t in type_]

    new_pokemon = {
        "name": {
            "english": name
        },
        "level": level,
        "type": type_,
        "base": {
            "HP": int(input("HP: ")),
            "Attack": int(input("Attack: ")),
            "Defense": int(input("Defense: ")),
            "Sp. Attack": int(input("Esp. Attack: ")),
            "Sp. Defense": int(input("Esp. Defense: ")),
            "Speed": int(input("Speed: "))
        }
    }

    list_pokemon.append(new_pokemon)

    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(list_pokemon, file, indent=2, ensure_ascii=False)
    
    print(f"\n¡{name} it has been successfully added to the Pokedex!")


add_pokemon()