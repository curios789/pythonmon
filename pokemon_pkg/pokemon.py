from decimal import DecimalException
import requests
api_url = "https://pokeapi.co/api/v2/"
post_url = "http://localhost:5000/"
#### GET DESCRIPTION FOR DEX ####
def pull_desc(pkmn):
    response = requests.get(api_url + "pokemon-species/" + pkmn.name)
    jsonResponse = response.json()
    x = 0
    while True:
        if (jsonResponse['flavor_text_entries'][x]['language']['name'] == "en"):
            return jsonResponse['flavor_text_entries'][x]['flavor_text']
        else:
            x = x + 1
#### ADD CAUGHT POKEMON TO DEX ####
def caught(pkmn):
    description = pull_desc(pkmn)
    print(pkmn.name)
    get_url = post_url + "pokedex/" + pkmn.name + "/"
    seen_before = requests.get(get_url)
    if seen_before.text == "False":
        new_pkmn = {'name': pkmn.name, 'description': description, "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/" + str(pkmn.number) + ".png", "seen": True, "caught": True, "dex_id": pkmn.id}
        requests.post(post_url + "pokedex/add/", json = new_pkmn)
#### ADD SEEN POKEMON TO DEX ####
def seen(pkmn):
    description = pull_desc(pkmn)
    seen_before = requests.get(post_url + "pokedex/" + pkmn.name + "/")
    if seen_before.text == "False":
        new_pkmn = {'name': pkmn.name, 'description': description, "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/" + str(pkmn.number) + ".png", "seen": True, "caught": False, "dex_id": pkmn.id}
        requests.post(post_url + "pokedex/add/", json = new_pkmn)

class Pokemon:
    """Create Pokemon"""
    def __init__(self, id):
        self.id = id
        self.response = requests.get(api_url + "pokemon/" + id)
        if self.response.status_code == 404:
            print("This pokemon does not exist. Please try again.")
            self.error = "404"
        else:
            self.jsonResponse = self.response.json()
            ####### Get Name b/c sometimes input might be an int #######
            self.name = self.jsonResponse['name']
            self.number = self.jsonResponse['id']
            ####### Assign Stats #######################################
            self.hp = self.jsonResponse['stats'][0]['base_stat']
            self.max_hp = self.jsonResponse['stats'][0]['base_stat']
            self.att = self.jsonResponse['stats'][1]['base_stat']
            self.defense = self.jsonResponse['stats'][2]['base_stat']
            self.sp_att = self.jsonResponse['stats'][3]['base_stat']
            self.sp_def = self.jsonResponse['stats'][4]['base_stat']
            self.speed = self.jsonResponse['stats'][5]['base_stat']
            self.num_types = len(self.jsonResponse['types'])
            self.type1 = self.jsonResponse['types'][0]['type']['name']
            if self.num_types == 2:
                self.type2 = self.jsonResponse['types'][1]['type']['name']
            self.num_moves = len(self.jsonResponse['moves'])
            self.selected_moves = []
            self.available_moves =  self.jsonResponse['moves']

    def get_moves(self, id):
        move = {}
        for x in id:
            response = requests.get(api_url + "move/" + str(x))
            response = response.json()
            if response['power'] != None:
                move[response['name']] = { "name": response['name'], "power": response['power'], "pp": response['pp'], "accuracy": response["accuracy"], "type": response['type']['name'], "damage_class": response["damage_class"], 'stat_changes': response["stat_changes"], 'meta-data': response['meta']}
        return move
    def check_moves(self, id):
        response = requests.get(id)
        response = response.json()
        if response['power'] != None:
           return response['name']


class EnemyPokemon(Pokemon):
    def __init__(self, id):
        super().__init__(id)
    def random_move(self, x):
        move = {}
        response = requests.get(api_url + "move/" + str(x))
        response = response.json()
        move = { "name": response['name'], "power": response['power'], "pp": response['pp'], "accuracy": response["accuracy"], "type": response['type']['name'], "damage_class": response["damage_class"], 'stat_changes': response["stat_changes"], 'meta-data': response['meta']}
        return move