# Pokedex
This script allows you to search for information about a Pokemon, given its name. The script will return the weight, height, types, abilities, moves, and URL of the Pokemon. It will also display an image of the Pokemon and create a .json file with the information. The Pokédex retrieves detailed data and images of Pokémon from the https://pokeapi.co/ web service via HTTP requests.

## Requirements

To use the project, you will need the following libraries:
- requests
- json
- os
- Pil
- matplotlib

You will also need to have access to the Pokeapi web service, which exposes detailed data and images of all Pokémon.

## Installation

1. Clone this repository: `git clone [https://github.com/your_username/pokemon-search.git]`
3. Install dependencies: `pip install requests Pillow matplotlib`
4. Run the script: `python pokemon_search.py`
5. Enter the name of the Pokemon you want to search for ID or Name

## Usage

The Pokédex allows you to search for information about any Pokémon by entering its name or ID. The search results will include details about the Pokémon, such as its type, abilities, stats, and an image of the Pokémon. The project uses Request, functions, and json to retrieve the data, and matplotlib to display the Pokémon image.

## Examples

Here are some sample results from searching for a few Pokémon:

- Name: Pikachu
- Weight: 60 g
- Height: 4 m
- Types: electric
- Abilities: static, lightning-rod
- Moves: mega-punch, pay-day, thunder-punch, slam, double-kick, mega-kick, headbutt, body-slam, take-down, double-edge, tail-whip, growl, surf, submission, counter, seismic-toss, strength, thunder-shock, thunderbolt, thunder-wave, thunder, dig, toxic, agility, quick-attack, rage, mimic, double-team, defense-curl, light-screen, reflect, bide, swift, skull-bash, flash, rest, substitute, thief, snore, curse, reversal, protect, sweet-kiss, mud-slap, zap-cannon, detect, endure, charm, rollout, swagger, spark, attract, sleep-talk, return, frustration, dynamic-punch, encore, iron-tail, hidden-power, rain-dance, rock-smash, uproar, facade, focus-punch, helping-hand, brick-break, knock-off, secret-power, fake-tears, signal-beam, covet, volt-tackle, calm-mind, shock-wave, natural-gift, feint, fling, magnet-rise, nasty-plot, discharge, captivate, grass-knot, charge-beam, electro-ball, round, echoed-voice, volt-switch, electroweb, wild-charge, disarming-voice, draining-kiss, play-rough, play-nice, confide, eerie-impulse, electric-terrain, nuzzle, laser-focus, rising-voltage, tera-blast
- URL: https://pokeapi.co/api/v2/pokemon/25

![imagen](https://user-images.githubusercontent.com/122582810/233002184-9dc863d2-cd14-44ae-8d13-18782b99a126.png)


## What We Learned

This project taught us how to build a Pokédex using HTTP requests, functions, and json. The most challenging aspect of the project was displaying the Pokémon image, which we achieved using the matplotlib library.
