# This is the battle package --- will contain all the functions that run battles
import random


class Battle:
    """THIS IS THE BATTLE CLASS"""
    def __init__(self, team):
        self.team = team
        self.effective_arr = []
    def switch_pokemon(self, team, active):
        """This switches Pokemon"""
        self.active = active
        for count, value in enumerate(team):
            print(str(count + 1) + ")", value.name)
        new_poke = input("Which Pokemon will you send out now?")
        return team[int(new_poke) - 1]

    def calculate_power(self, pokemon, move, opp_pokemon):
        """This function calculates the move damage"""
        self.move = move
        # Check if move is a special attack or a regular attack and use correct stats based on this
        if self.move['damage_class']['name'] == "special":
            attack = pokemon.sp_att
            defense = pokemon.sp_def
        else:
            attack = opp_pokemon.att
            defense = opp_pokemon.defense
        if hasattr(pokemon, 'type2'):
            if pokemon.type2 == self.move['type']:
                stab = 1.5
        if pokemon.type1 == self.move['type']:
            stab = 1.5
        else:
            stab = 1
        ################################################### TYPE EFFECTIVENESS ##################################################################
        if self.move['type'] == "normal":  # NORMAL
            self.effective_arr = {"normal": 1, "fire": 1, "water": 1, "electric": 1, "grass": 1, "ice": 1, "fighting": 1, "poison": 1,
                                  "ground": 1, "flying": 1, "psychic": 1, "bug": 1, "rock": 0.5, "ghost": 0, "dragon": 1, "dark": 1, "steel": 0.5, "fairy": 1}
        elif self.move['type'] == "fire":  # FIRE
            self.effective_arr = {"normal": 1, "fire": 0.5, "water": 0.5, "electric": 1, "grass": 2, "ice": 2, "fighting": 1, "poison": 1,
                                  "ground": 1, "flying": 1, "psychic": 1, "bug": 2, "rock": 0.5, "ghost": 1, "dragon": 0.5, "dark": 1, "steel": 2, "fairy": 1}
        elif self.move['type'] == "water":  # WATER
            self.effective_arr = {"normal": 1, "fire": 2, "water": 0.5, "electric": 1, "grass": 0.5, "ice": 1, "fighting": 1, "poison": 1,
                                  "ground": 1, "flying": 1, "psychic": 1, "bug": 1, "rock": 2, "ghost": 1, "dragon": 0.5, "dark": 1, "steel": 1, "fairy": 1}
        elif self.move['type'] == "electric":  # ELECTRIC
            self.effective_arr = {"normal": 1, "fire": 1, "water": 2, "electric": 0.5, "grass": 0.5, "ice": 1, "fighting": 1, "poison": 1,
                                  "ground": 0, "flying": 2, "psychic": 1, "bug": 1, "rock": 1, "ghost": 1, "dragon": 0.5, "dark": 1, "steel": 1, "fairy": 1}
        elif self.move['type'] == "grass":  # GRASS
            self.effective_arr = {"normal": 1, "fire": 0.5, "water": 2, "electric": 1, "grass": 0.5, "ice": 1, "fighting": 1, "poison": 0.5,
                                  "ground": 2, "flying": 0.5, "psychic": 1, "bug": 0.5, "rock": 2, "ghost": 1, "dragon": 0.5, "dark": 1, "steel": 0.5, "fairy": 1}
        elif self.move['type'] == "ice":  # ICE
            self.effective_arr = {"normal": 1, "fire": 0.5, "water": 0.5, "electric": 1, "grass": 2, "ice": 0.5, "fighting": 1, "poison": 1,
                                  "ground": 2, "flying": 2, "psychic": 1, "bug": 1, "rock": 1, "ghost": 1, "dragon": 2, "dark": 1, "steel": 0.5, "fairy": 1}
        elif self.move['type'] == "fighting":  # FIGHTING
            self.effective_arr = {"normal": 2, "fire": 1, "water": 1, "electric": 1, "grass": 1, "ice": 2, "fighting": 1, "poison": 0.5,
                                  "ground": 1, "flying": 0.5, "psychic": 0.5, "bug": 0.5, "rock": 2, "ghost": 0, "dragon": 1, "dark": 2, "steel": 2, "fairy": 0.5}
        elif self.move['type'] == "poison":  # POISON
            self.effective_arr = {"normal": 1, "fire": 1, "water": 1, "electric": 1, "grass": 2, "ice": 1, "fighting": 1, "poison": 0.5,
                                  "ground": 0.5, "flying": 1, "psychic": 1, "bug": 1, "rock": 0.5, "ghost": 0.5, "dragon": 1, "dark": 1, "steel": 0, "fairy": 2}
        elif self.move['type'] == "ground":  # GROUND
            self.effective_arr = {"normal": 1, "fire": 2, "water": 1, "electric": 2, "grass": 0.5, "ice": 1, "fighting": 1, "poison": 2,
                                  "ground": 1, "flying": 0, "psychic": 1, "bug": 0.5, "rock": 2, "ghost": 1, "dragon": 1, "dark": 1, "steel": 2, "fairy": 1}
        elif self.move['type'] == "flying":  # FLYING
            self.effective_arr = {"normal": 1, "fire": 1, "water": 1, "electric": 0.5, "grass": 2, "ice": 1, "fighting": 2, "poison": 1,
                                  "ground": 1, "flying": 1, "psychic": 1, "bug": 2, "rock": 0.5, "ghost": 1, "dragon": 1, "dark": 1, "steel": 0.5, "fairy": 1}
        elif self.move['type'] == "pyschic":  # PSYCHIC
            self.effective_arr = {"normal": 1, "fire": 1, "water": 1, "electric": 1, "grass": 1, "ice": 1, "fighting": 2, "poison": 2,
                                  "ground": 1, "flying": 1, "psychic": 0.5, "bug": 1, "rock": 1, "ghost": 1, "dragon": 1, "dark": 0, "steel": 0.5, "fairy": 1}
        elif self.move['type'] == "bug":  # BUGTYPE
            self.effective_arr = {"normal": 1, "fire": 0.5, "water": 1, "electric": 1, "grass": 2, "ice": 1, "fighting": 0.5, "poison": 0.5,
                                  "ground": 1, "flying": 0.5, "psychic": 2, "bug": 1, "rock": 1, "ghost": 0.5, "dragon": 1, "dark": 2, "steel": 0.5, "fairy": 0.5}
        elif self.move['type'] == "rock":  # ROCK
            self.effective_arr = {"normal": 1, "fire": 2, "water": 1, "electric": 1, "grass": 1, "ice": 2, "fighting": 0.5, "poison": 1,
                                  "ground": 0.5, "flying": 2, "psychic": 1, "bug": 2, "rock": 1, "ghost": 1, "dragon": 1, "dark": 1, "steel": 0.5, "fairy": 1}
        elif self.move['type'] == "ghost":  # GHOST
            self.effective_arr = {"normal": 0, "fire": 1, "water": 1, "electric": 1, "grass": 1, "ice": 1, "fighting": 1, "poison": 1,
                                  "ground": 1, "flying": 1, "psychic": 2, "bug": 1, "rock": 1, "ghost": 2, "dragon": 1, "dark": 0.5, "steel": 1, "fairy": 1}
        elif self.move['type'] == "dragon":  # DRAGON
            self.effective_arr = {"normal": 1, "fire": 1, "water": 1, "electric": 1, "grass": 1, "ice": 1, "fighting": 1, "poison": 1,
                                  "ground": 1, "flying": 1, "psychic": 1, "bug": 1, "rock": 1, "ghost": 1, "dragon": 1, "dark": 1, "steel": 1, "fairy": 1}
        elif self.move['type'] == "dark":  # DARK
            self.effective_arr = {"normal": 1, "fire": 1, "water": 1, "electric": 1, "grass": 1, "ice": 1, "fighting": 1, "poison": 1,
                                  "ground": 1, "flying": 1, "psychic": 1, "bug": 1, "rock": 1, "ghost": 1, "dragon": 1, "dark": 1, "steel": 1, "fairy": 1}
        elif self.move['type'] == "steel":  # STEEL
            self.effective_arr = {"normal": 1, "fire": 0.5, "water": 0.5, "electric": 0.5, "grass": 1, "ice": 2, "fighting": 1, "poison": 1,
                                  "ground": 1, "flying": 1, "psychic": 1, "bug": 1, "rock": 2, "ghost": 1, "dragon": 1, "dark": 1, "steel": 0.5, "fairy": 2}
        elif self.move['type'] == "fairy":  # FAIRY
            self.effective_arr = {"normal": 1, "fire": 0.5, "water": 1, "electric": 1, "grass": 1, "ice": 1, "fighting": 2, "poison": 0.5,
                                  "ground": 1, "flying": 1, "psychic": 1, "bug": 1, "rock": 1, "ghost": 1, "dragon": 2, "dark": 2, "steel": 0.5, "fairy": 1}
        self.type1 = self.effective_arr[opp_pokemon.type1]
        if hasattr(opp_pokemon, "type2"):
            self.type2 = self.effective_arr[opp_pokemon.type2]
        else:
            self.type2 = 1
        self.type = self.type1 * self.type2

        ### THIS IS THE CALCULATION #############################################################################################################
        #########################################################################################################################################
        ###################### WHAT IF IT'S MULTIPLE HITS? ######################################################################################
        if move['meta-data']['min_hits'] is not None:
            min_hits = move['meta-data']['min_hits']
            max_hits = move['meta-data']['max_hits']
            hit_times = random.randint(min_hits, max_hits)
            total_damage = 0
            print(move['name'], "hit", hit_times, "times!")
            for n in range(0, hit_times, 1):
                damage = int((((((2 / 5) + 2) * self.move['power'] * attack / defense) /
                               50) + 2) * (random.randint(217, 255) / 255) * stab * self.type)
                print("Hit", str(n + 1) + ":", str(damage))
                total_damage += damage
            return total_damage
        else:
            damage = int((((((2 / 5) + 2) * self.move['power'] * attack / defense) /
                           50) + 2) * (random.randint(217, 255) / 255) * stab * self.type)
            print(pokemon.name, "used", move['name'] + "!")
            if self.type == 0.25 or self.type == 0.5:
                print("The move was not very effective...")
            elif self.type == 2 or self.type == 4:
                print("The move was super effective!")
            elif self.type == 0:
                print("The move had no effect...")
            return damage
    def turn(self, active, opp_poke):
        """Player Turn"""
        self.active = active
        self.active_hp = self.active.hp
        self.opp_poke = opp_poke
        self.opp_poke_hp = self.opp_poke.hp
        x = 0
        # Print the available moves for selected Pokemon
        for move_name in active.selected_moves.values():
            x += 1
            print(str(x) + ")", move_name['name'], "-", move_name['type'],
                  "-", move_name['power'], "-", move_name['pp'])
        choice = input("Which move will you use? ")
        keys_list = list(active.selected_moves)
        # This allows you to make a numeric choice. This is way easier than having the user type the name - No spelling errors.
        print(keys_list[int(choice) - 1])
        choice_string = self.active.selected_moves[str(
            keys_list[int(choice) - 1])]
        damage = self.calculate_power(active, choice_string, opp_poke)
        self.opp_poke.hp = self.opp_poke.hp - damage
        print(self.opp_poke.name, "HP:", self.opp_poke_hp)

    def enemy_turn(self, active, wild):
        """Opponent's turn"""
        self.active = active
        self.opp_active = wild
        # Cycle through available move list until we find a move that does damage
        while True:
            randnum = random.randint(0, wild.num_moves)
            enemy_move = wild.check_moves(
                wild.available_moves[randnum]['move']['url'])
            if enemy_move is not None:
                enemy_move = wild.random_move(enemy_move)
                break
        # Calculate the damage
        damage = self.calculate_power(self.opp_active, enemy_move, active)
        self.team[0].hp -= damage
        print(self.active.name, " HP:", self.active.hp)


class Wild(Battle):
    """This ckass is for battles in the wild"""
    def __init__(self, team, wild):
        self.team = team
        self.wild = wild
        self.wild_hp = self.wild.hp
        print("You have run into a wild\033[035m",
              self.wild.name.capitalize() + "!\033[0m")
        print("HP:", self.wild_hp, "\n")
        print("You send out\033[032m", team[0].name.capitalize() + "\033[0m")
        self.active = team[0]
        super().__init__(team)



class Trainer(Battle):
    """This class is for trainer battles"""
    def __init__(self, team, opp_active):
        self.team = team
        self.opp_active = opp_active
        self.active = team[0]
        self.active_hp = self.active.hp
        super().__init__(team)
        print("Trainer sends out", self.opp_active.name)
        print("HP:", self.opp_active.hp)
        print("You send out", self.active.name)
