import random
from pokemon_pkg import pokemon, battle


class EnemyTeam:
    def __init__(self, value):
        self.value = value
        self.next = None
###################################### DISPLAY THE TEAM ##########################################
def display_team(pkmn):
    print("\033[33m=============================================")
    print("                 ",pkmn.name.capitalize(),"                ")
    print("=============================================\033[0m")
    if pkmn.num_types == 2:
        print("\033[36m******* TYPE:", pkmn.type1, "/", pkmn.type2, "*******\033[0m")
    else:
        print("\033[36m************ TYPE:",pkmn.type1, "***************\033[0m")
    print("HP:", pkmn.hp,"         Attack:",pkmn.att, "     Defense:", pkmn.defense)
    print("Sp Att:", pkmn.sp_att,"     Sp Def:",pkmn.sp_def, "   Speed:", pkmn.speed)
    movekeys = []
    available_moves = pkmn.num_moves
    if int(available_moves) > 4:
        total_moves = 4
    else:
        total_moves = available_moves
    while (len(movekeys) <= (total_moves - 1)):
        randnum = random.randint(0, (int(available_moves) - 1))
        move = pkmn.check_moves(pkmn.available_moves[randnum]['move']['url'])
        if move != None:
            movekeys.append(move)
    moves = pkmn.get_moves(movekeys)
    pkmn.selected_moves = moves
    print("\033[36m=============== MOVE LIST ===============\033[0m")
    for move_name in moves.values():
        print(move_name['name'], "-", move_name['pp'], "PP")




###################################### SET UP THE TEAM ##########################################
#1) Request input from player
#2) Call the PokeAPI based on player choices
#3) Assign API JSON data to team variables
team = []
while True:
    poke1 = input("Please type the name of a Pokemon (or type Random Team to select 5 random Pokemon)")
    if poke1.lower() == "random team":
        poke1 = str(random.randint(1,800))
        team.append(pokemon.Pokemon(poke1))
        poke2 = str(random.randint(1,800))
        team.append(pokemon.Pokemon(poke2))
        poke3 = str(random.randint(1,800))
        team.append(pokemon.Pokemon(poke3))
        poke4 = str(random.randint(1,800))
        team.append(pokemon.Pokemon(poke4))
        poke5 = str(random.randint(1,800))
        team.append(pokemon.Pokemon(poke5))
        for x in range(0,5):
            display_team(team[x])
            pokemon.caught(team[x])
        break
    else:
        if hasattr(pokemon.Pokemon(poke1),"error"):
            continue
        else:
            team.append(pokemon.Pokemon(poke1))
        display_team(team[0])
        pokemon.caught(team[0])
        while True:
            poke2 = input("Please type the name of a Pokemon:")
            if hasattr(pokemon.Pokemon(poke2),"error"):
                continue
            else:
                team.append(pokemon.Pokemon(poke2))
                break
        display_team(team[1])
        pokemon.caught(team[1])
        while True:
            poke3 = input("Please type the name of a Pokemon:")
            if hasattr(pokemon.Pokemon(poke3),"error"):
                continue
            else:
                team.append(pokemon.Pokemon(poke3))
                break
        display_team(team[2])
        pokemon.caught(team[2])
        while True:
            poke4 = input("Please type the name of a Pokemon:")
            if hasattr(pokemon.Pokemon(poke4),"error"):
                continue
            else:
                team.append(pokemon.Pokemon(poke4))
                break
        display_team(team[3])
        pokemon.caught(team[3])
        while True:
            poke5 = input("Please type the name of a Pokemon:")
            if hasattr(pokemon.Pokemon(poke5),"error"):
                continue
            else:
                team.append(pokemon.Pokemon(poke5))
                break
        display_team(team[4])
        pokemon.caught(team[4])
    break


################################################################################################
################## I wanna be the very best, like no one ever was ##############################
################################################################################################
while True:
    print("Your Pokemon journey begins here! What will you do? \n 1) Explore \n 2) Battle Trainer \n 3) Visit PokeCenter \n 4) Quit")
    user_choice = input("Choose an option: ")
    if user_choice == "1":
        enemy = pokemon.EnemyPokemon(str(random.randint(1,800)))
        pokemon.seen(enemy)
        print("You begin to explore...\n")
        wild_battle = battle.Wild(team,enemy)
        active = wild_battle.active
        while True:
            if (wild_battle.wild_hp <= 0):
                print(wild_battle.wild.name, "has fainted!")
                break
            elif (wild_battle.active.hp <= 0):
                if len(wild_battle.team) == 0:
                    print("Your team has fainted!")
                    break
                else:
                    print(wild_battle.active.name, "has fainted! Choose next Pokemon")
                    active = wild_battle.switch_pokemon(wild_battle.team, active)
            print("\n\033[032m======== YOUR TURN ========\033[0m")
            print("1. Fight\n2. Switch Pokemon\n3. Try to catch\n4. Run Away")
            choice = input("What will you do?")
            if choice == "1":
                #fight
                wild_battle.turn(active, wild_battle.wild)
                print("\033[035m======== OPPONENT'S TURN ========\033[0m")
                wild_battle.enemy_turn(active, enemy)
            if choice == "2":
                #switch pokemon
                print(active.name + ", return!")
                active = wild_battle.switch_pokemon(wild_battle.team,active)
                print("Go,", active.name + "!")
            if choice == "3":
                #the catch function!
                f = battle.try_catch(wild_battle.wild, wild_battle.wild_hp,"pokeball")
                if (f == "caught"):
                    break
            if choice == "4":
                #run away
                print("You run away....")
                break
        #write explore function
    elif user_choice == "2":
        print("1. Brock \n2. Misty \n3. Gary")
        trainer_choice = input("Who will you challenge? (Choose 1-4) ")
        if trainer_choice == "1":
            trainer = [pokemon.EnemyPokemon("geodude"), pokemon.EnemyPokemon("onix"), pokemon.EnemyPokemon("tyranitar")]
        if trainer_choice == "2":
            trainer = [pokemon.EnemyPokemon("starmie"), pokemon.EnemyPokemon("golduck"), pokemon.EnemyPokemon("slowbro")]
        if trainer_choice == "3":
            trainer = [pokemon.EnemyPokemon("arcanine"), pokemon.EnemyPokemon("golem"), pokemon.EnemyPokemon("nidoking"), pokemon.EnemyPokemon("arceus")]
        for item, value in enumerate(trainer):
            display_team(value)
        opp_active = trainer[0]
        print("")
        trainer_battle = battle.Trainer(team, opp_active)
        while True:
            print("======== YOUR TURN ========")
            print("1. Fight\n2. Switch Pokemon")
            choice = input("What will you do?")
            if choice == "1":
                #fight
                trainer_battle.turn(trainer_battle.active, trainer_battle.opp_active)
                if (trainer_battle.opp_poke_hp <= 0):
                    print(trainer_battle.opp_active.name, "has fainted!")
                    if len(trainer) != 1:
                        trainer_battle.opp_active = trainer[1]
                        trainer_battle.opp_poke_hp = trainer[1].hp
                        trainer.pop(0)
                        print("Trainer sends out", trainer_battle.opp_active.name)
                    else:
                        print("You have defeated the trainer!")
                        break
                trainer_battle.enemy_turn(trainer_battle.active, trainer_battle.opp_active)
                if trainer_battle.active_hp <= 0:
                    print(trainer_battle.active.name + " has fainted.")
                    trainer_battle.active = trainer_battle.switch_pokemon(trainer_battle.team,trainer_battle.active)
                    print("Go,", trainer_battle.active.name + "!")
            elif choice == "2":
                #switch pokemon
                print(trainer_battle.active.name + ", return!")
                trainer_battle.active = trainer_battle.switch_pokemon(trainer_battle.team,trainer_battle.active)
                trainer_battle.active_hp = trainer_battle.active.hp
                print("Go,", trainer_battle.active.name + "!")
            
            
        
        #write battle function
    elif user_choice == "3":
        print("Heal your Pokemon?")
        #write heal function
        for x in range(0,5):
            team[x].hp = team[x].max_hp
        print("Your Pokemon have been healed!")
    elif user_choice == "4":
        print("\033[33mSo sorry to see you go. Your Pokemon have been set free.\033[0m")
        quit()
    else:
        print("Please choose an option 1-4.")