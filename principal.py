from src.dao.pokemon_dao import PokemonDAO
from src.classes.pokemon import Pokemon
from src.bd.bd_connection import new_banco_de_dados


new_pokemon = Pokemon(1, 'Pikachu', 'Elétrico', '0.4', '6', '90')
new_pokemon_dao = PokemonDAO(new_pokemon)
new_banco_de_dados.insert_in_BD(new_pokemon_dao._pokemon_json)


new_pokemon = Pokemon(2,'Charizard', 'fogo', '0.5', '7','70')
new_pokemon_dao = PokemonDAO(new_pokemon)
new_banco_de_dados.insert_in_BD(new_pokemon_dao._pokemon_json)

new_pokemon = Pokemon(3,'Alakazan', 'psiquicos', '1', '8', '100')
new_pokemon_dao = PokemonDAO(new_pokemon)
new_banco_de_dados.insert_in_BD(new_pokemon_dao._pokemon_json)