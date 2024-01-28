import requests

api_pokemon = 'http://pokeapi.co/api/v2/pokemon/1'

r = requests.get(api_pokemon)

assert r.status_code == 200
