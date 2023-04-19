import requests
import json
import os
from PIL import Image
from io import BytesIO
import matplotlib.pyplot as plt

def main():
    # Get the name or ID of the Pokémon
    pokemon = input("Enter the name or ID of a Pokémon: ")

    # Check if the input is a number or a string
    if pokemon.isdigit():
        # Query the Pokémon information by ID
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}")
        if response.status_code == 404:
            print(f"Pokemon with ID {pokemon} not found.")
            return
        pokemon_info = response.json()
        pokemon_name = pokemon_info["name"]
    else:
        # Query the Pokémon information by name
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}")
        if response.status_code == 404:
            print(f"Pokemon {pokemon} not found.")
            return
        pokemon_info = response.json()
        pokemon_name = pokemon_info["name"]

    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_info['id']}"

    # Get the weight, height, types, abilities, and moves of the Pokémon
    weight = pokemon_info["weight"]
    height = pokemon_info["height"]
    types = [t["type"]["name"] for t in pokemon_info["types"]]
    abilities = [a["ability"]["name"] for a in pokemon_info["abilities"]]
    moves = [m["move"]["name"] for m in pokemon_info["moves"]]
    image_url = pokemon_info["sprites"]["front_default"]

    # Print the Pokémon information
    print(f"Name: {pokemon_name.capitalize()}")
    print(f"Weight: {weight} g")
    print(f"Height: {height} m")
    print(f"Types: {', '.join(types)}")
    print(f"Abilities: {', '.join(abilities)}")
    print(f"Moves: {', '.join(moves)}")
    print(f"URL: {url}")

    # Get and show the Pokémon image
    response_image = requests.get(image_url)
    if response_image.status_code == 200:
        image = Image.open(BytesIO(response_image.content))
        plt.imshow(image)
        plt.show()

    # Create a .json file with the Pokémon information
    if not os.path.exists('pokedex'):
        os.mkdir('pokedex')
    with open(f"pokedex/{pokemon_name}.json", "w") as file:
        json.dump({
            'name': pokemon_name.capitalize(),
            'url': url,
            'image': image_url,
            'weight': weight,
            'height': height,
            'types': types,
            'abilities': abilities,
            'moves': moves
        }, file, indent=4)

if __name__ == "__main__":
    main()
#%%
