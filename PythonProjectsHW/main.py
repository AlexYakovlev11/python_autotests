import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '****'
HEADER = {'Content-Type': 'application/json', 'trainer_token' : TOKEN}
BODY_CREATE_POKEMON = {
    "name": "Гайкозавр",
    "photo_id": 31
}


RESPONSE_CREATE = requests.post(url = f'{URL}/pokemons', headers=HEADER, json=BODY_CREATE_POKEMON)
print(RESPONSE_CREATE.text)

"""добавляем id в переменную"""

pokemon_id = RESPONSE_CREATE.json()['id'] 
print(pokemon_id)

BODY_CHANGE_NAME = {
    "pokemon_id": pokemon_id,
    "name": "Болтозавр",
    "photo_id": 31
}

RESPONSE_CH_NAME= requests.put(url = f'{URL}/pokemons', headers= HEADER, json = BODY_CHANGE_NAME)
print(RESPONSE_CH_NAME.text)


BODY_ADD_POKEMON = {
    "pokemon_id": pokemon_id
}

RESPONSE__ADD = requests.post(url = f'{URL}/trainers/add_pokeball', headers= HEADER, json = BODY_ADD_POKEMON)
print(RESPONSE__ADD.text)



