import random

from Enemy import *
from Player import *
from Globals import *


def start_program():
    players = []

    access_charactersheets = False
    access_calculations = False
    access_enemy_generation = False

    set_original_soul_shard_chance = 0.005
    # original_soul_shard_chance
    # soul_shard_chance
    established_soul_shard_vars = False
    soul_shard_chance_increase = 0.0025

    in_program = True

    while in_program:
        print("1. Access Character Sheets")
        print("2. Perform Calculation")
        print("3. Generate Enemy")
        print("4. Exit")
        choice = get_input("int", [1, 4])
        if choice == 1:
            access_charactersheets = True
        elif choice == 2:
            access_calculations = True
        elif choice == 3:
            access_enemy_generation = True
        elif choice == 4:
            if len(players) > 0:
                confirming_exit = True
            else:
                confirming_exit = False
                in_program = False
            while confirming_exit:
                print("Are you sure you want to exit?")
                print("1. Yes")
                print("2. No")
                choice = get_input("int", [1, 2])
                if choice == 1:
                    confirming_exit = False
                    in_program = False
                elif choice == 2:
                    confirming_exit = False

        while access_charactersheets:
            print("1. Create Character")
            print("2. Access Player Inventory")
            print("3. Change Player Stats")
            print("4. Go Back")
            choice = get_input("int", [1, 4])
            if choice == 1:
                players.append(Player())
            elif choice == 2:
                if len(players) == 0:
                    print("There currently exist no players.")
                    inventory_accessing = False
                else:
                    inventory_accessing = True

                while inventory_accessing:
                    player_index = 0
                    inventory_browsing = True

                    print("Which player's inventory do you want to access?")
                    for player_index in range(len(players)):
                        print(str(player_index + 1) + ". " + players[player_index].name)
                    print(str(player_index + 2) + ". Go Back")
                    player_choice = get_input("int", [1, player_index + 2])

                    if player_choice == player_index + 2:
                        inventory_accessing = False
                        inventory_browsing = False

                    player_choice -= 1
                    while inventory_browsing:
                        print("-----" + players[player_choice].name + "-----")
                        print("Coins: " + str(players[player_choice].coins))
                        print("Mass: " + str(players[player_choice].total_mass))
                        print("1. Show Inventory")
                        print("2. Add Item")
                        print("3. Remove Item")
                        print("4. Add/Remove Coins")
                        print("5. Go Back")
                        choice = get_input("int", [1, 5])

                        if choice == 1:
                            print()
                            print("Coins: " + str(players[player_choice].coins))
                            for item_index in range(len(players[player_choice].inventory)):
                                print(str(item_index + 1) + ". (" + str(
                                    players[player_choice].inventory[item_index][2]) + ") " +
                                      players[player_choice].inventory[item_index][0])
                            print()

                        elif choice == 2:
                            item_in_inventory = False
                            new_item = Player.get_item_info()
                            for item_index in range(len(players[player_choice].inventory)):
                                if new_item[0] == players[player_choice].inventory[item_index][0]:
                                    players[player_choice].inventory[item_index][2] += new_item[2]
                                    item_in_inventory = True
                            if not item_in_inventory:
                                players[player_choice].inventory.append(new_item)
                            players[player_choice].calculate_total_mass()

                        elif choice == 3:
                            for item_index in range(len(players[player_choice].inventory)):
                                print(str(item_index + 1) + ". (" + str(
                                    players[player_choice].inventory[item_index][2]) + ") " +
                                      players[player_choice].inventory[item_index][0])

                            item_choice = get_input("int", [1, item_index + 1])
                            print("How many do you want to remove?")
                            quantity_choice = get_input("int")
                            players[player_choice].inventory[item_choice - 1][2] -= quantity_choice
                            if players[player_choice].inventory[item_choice - 1][2] <= 0:
                                del players[player_choice].inventory[item_choice - 1]
                            players[player_choice].calculate_total_mass()

                        elif choice == 4:
                            print("How many coins to add/remove?")
                            players[player_choice].coins += get_input("int")
                            if players[player_choice].coins < 0: players[player_choice].coins = 0

                        elif choice == 5:
                            inventory_browsing = False

            elif choice == 3:
                if len(players) == 0:
                    print("There currently exist no players.")
                    stats_accessing = False
                else:
                    stats_accessing = True

                while stats_accessing:
                    player_index = 0
                    stats_browsing = True

                    print("Which player's stats do you want to access?")
                    for player_index in range(len(players)):
                        print(str(player_index + 1) + ". " + players[player_index].name)
                    print(str(player_index + 2) + ". Go Back")
                    player_choice = get_input("int", [1, player_index + 2])

                    if player_choice == player_index + 2:
                        stats_accessing = False
                        stats_browsing = False

                    player_choice -= 1
                    while stats_browsing:
                        print("-----" + players[player_choice].name + "-----")
                        print("Select a stat if you wish to change it.")
                        for i in range(len(players[player_choice].stats)):
                            print(str(i+1) + ". " + players[player_choice].stats[i][0] + " - " + str(players[player_choice].stats[i][1]))
                        print(str(i+2) + ". Go Back")
                        stats_choice = get_input("int", [1, i+2])

                        if stats_choice == i+2:
                            stats_browsing = False
                        else:
                            stats_choice -= 1
                            print("Enter " + players[player_choice].name + "'s new " + players[player_choice].stats[stats_choice][0] + ".")
                            players[player_choice].stats[stats_choice][1] = get_input("int", [0, 2147483647])

            elif choice == 4:
                access_charactersheets = False

        while access_enemy_generation:
            enemies = [
                JeranPython(),
                JeranFlawn(),
                AgitatedOrangutan(),
                Faethling(),
                TallonArcher(),
                TallonSoldier(),
                TallonShipCaptain(),
                GoblinKnifethrower(),
                GoblinCamouflager(),
                TallonMage(),
                TallonWarlock(),
                TallonMissionCommander(),
                AmbolGuard(),
                CommanderFinch(),
                CrawlingCod(),
                TideberthCavernNaga(),
                TideberthAssassin(),
                TideberthMage(),
                TideberthSorcerer(),
                TideberthCorrupter(),
                TideberthCavernMonster(),
                TideberthWaterElemental(),
                TideberthMimic(),
                HeadTideberthMagus(),
                CavernousSnappingPlant(),
                GorsonLion(),
                GorsonKodo(),
                LargeGorsonAnt()
            ]

            print("Which enemy would you like to generate?")
            enemy_name = get_input("string")

            for enemy in enemies:
                if enemy.name == enemy_name:
                    break

            enemy.print_info()

            print("1. Generate Another")
            print("2. Go Back")
            choice = get_input("int", [1, 2])

            if choice == 2:
                access_enemy_generation = False

        while access_calculations:
            print("What would you like to calculate?")
            print("1. Sequence")
            print("2. Magic Accuracy")
            print("3. Non-Magic Accuracy")
            print("4. Melee Accuracy")
            print("5. XP Required for Next Level")
            print("6. Chance to Block")
            print("7. Chance to Surrender")
            print("8. Sneak Chance")
            print("9. Calculate Skills & Professions")
            print("10. Check Soul Shard Drop")
            print("11. Weapon Contest")
            print("12. Go Back")
            num = get_input("int", [1, 12])

            if num == 1:
                if not len(players) == 0:
                    data_choice = str(input("Use saved player data? y/n: "))
                    if data_choice == "n":
                        data_choice = False
                    else:
                        data_choice = True
                else:
                    data_choice = False

                print("How many combatants are there?")
                sequence_combatants = []
                player_num = get_input("int", [1, 2147483647])
                for a in range(0, player_num):
                    print("What is the name of combatant #" + str(a + 1) + "?")
                    name_of_player = get_input("string")
                    sequence_combatants.append(name_of_player)
                combatant_sequence = []
                for a in range(0, player_num):
                    is_player = False
                    for player in players:
                        if player.name == sequence_combatants[a]:
                            dexterity = player.get_stat("Dexterity")
                            is_player = True
                    if not is_player or not data_choice:
                        print("What is " + sequence_combatants[a] + "'s dexterity?")
                        dexterity = get_input("int")
                    ind_sequence = random.uniform(0, 7) + dexterity
                    combatant_sequence.append(ind_sequence)
                for a in range(0, player_num):
                    print(sequence_combatants[a] + "'s sequence is " + str(round(combatant_sequence[a], 2)))

            elif num == 2 or num == 3:
                if not len(players) == 0:
                    data_choice = str(input("Use saved player data? y/n: "))
                    if data_choice == "n":
                        data_choice = False
                    else:
                        data_choice = True
                else:
                    data_choice = False

                if data_choice:
                    name_recognized = False
                    print("What is the player's name?")
                    while not name_recognized:
                        player_name_choice = get_input("string")
                        for player in players:
                            if player.name == player_name_choice:
                                name_recognized = True
                                player_in_combat = player
                        if not name_recognized:
                            print("That name is not recognized. Try again.")

                    print("Is " + player_in_combat.name + " the attacker or the target?")
                    print("1. Attacker")
                    print("2. Target")
                    it_choice = get_input("int", [1, 2])

                    # When player is attacker
                    if it_choice == 1:
                        p = player_in_combat.get_stat("Perception")

                        print("Target dexterity?")
                        ea = get_input("int")
                        print("Distance from " + player_in_combat.name + " to target?")
                        m = get_input("int", [0, 2147483647])
                        print("How many meters did the target move last turn?")
                        t = get_input("int", [0, 2147483647])
                        print("Square area number of target?")
                        s = get_input("int")

                    # When player is target
                    elif it_choice == 2:
                        ea = player_in_combat.get_stat("Dexterity")
                        s = player_in_combat.size

                        print("Attacker perception?")
                        p = get_input("int")
                        print("Distance from attacker to " + player_in_combat.name + "?")
                        m = get_input("int", [0, 2147483647])
                        print("How many meters did " + player_in_combat.name + " move last turn?")
                        t = get_input("int", [0, 2147483647])
                else:
                    print("Attacker perception?")
                    p = get_input("int")
                    print("Target dexterity?")
                    ea = get_input("int")
                    print("Distance from attacker to target?")
                    m = get_input("int", [0, 2147483647])
                    print("How many meters did the target move last turn?")
                    t = get_input("int", [0, 2147483647])
                    print("Square area number of target?")
                    s = get_input("int")

                print("Is the attacker aiming for a limb? (1 if yes, 0 if no)")
                l = get_input("int", [0, 1])
                if num == 2:
                    accuracy = 105 - 3 * m + 2 * (p - 5) - 3 * t - 2 * ea - 25 * l
                elif num == 3:
                    accuracy = 100 - 3 * m + 3 * (p - 5) - 3 * t - 2 * ea - 25 * l
                if s < 0:
                    accuracy += -abs((s - 1) ** (3 + l))  # Modify
                elif s > 0:
                    accuracy += (s + 1) ** (3 + l)
                elif s == 0:  # Useless condition
                    accuracy += s ** 3
                rand_num = random.randint(0, 99)

                print("Accuracy chance: " + str(accuracy))
                print()
                print("Was it a hit?")
                print("1. Yes")
                print("2. No")
                hit_choice = get_input("int", [1, 2])

                if hit_choice == 2:
                    print("How many other targets are in the attacker's line of sight?")
                    num_of_nearby = get_input("int", [0, 2147483647])
                    nearby_targets = []
                    for n in range(num_of_nearby):
                        target_data = []
                        print("What is the name of target #" + str(n + 1) + "?")
                        name_of_target = get_input("string")
                        target_data.append(name_of_target)
                        print("How far away is target #" + str(n + 1) + " from the original target?")
                        distance_from_target = get_input("int", [0, 2147483647])
                        target_data.append(distance_from_target)
                        nearby_targets.append(target_data)
                    nearby_targets = sorted(nearby_targets)
                    for t in nearby_targets:
                        chance_hit = 50 - t[1] * 4 - m * 3  # Review this formula later
                        print("The chance to hit " + t[0] + " is " + str(chance_hit) + ".")
            elif num == 4:
                if not len(players) == 0:
                    data_choice = str(input("Use saved player data? y/n: "))
                    if data_choice == "n":
                        data_choice = False
                    else:
                        data_choice = True
                else:
                    data_choice = False

                if data_choice:
                    name_recognized = False
                    print("What is the player's name?")
                    while not name_recognized:
                        player_name_choice = get_input("string")
                        for player in players:
                            if player.name == player_name_choice:
                                name_recognized = True
                                player_in_combat = player
                        if not name_recognized:
                            print("That name is not recognized. Try again.")

                    print("Is " + player_in_combat.name + " the attacker or the target?")
                    print("1. Attacker")
                    print("2. Target")
                    it_choice = get_input("int", [1, 2])

                    # When player is attacker
                    if it_choice == 1:
                        pa = player_in_combat.get_stat("Dexterity")
                        p = player_in_combat.get_stat("Perception")

                        print("Dexterity of target?")
                        ea = get_input("int")

                    # When player is target
                    elif it_choice == 2:
                        ea = player_in_combat.get_stat("Dexterity")

                        print("Dexterity of attacker?")
                        pa = get_input("int")
                        print("Perception of attacker?")
                        p = get_input("int")
                else:
                    print("Dexterity of target?")
                    ea = get_input("int")
                    print("Dexterity of attacker?")
                    pa = get_input("int")
                    print("Perception of attacker?")
                    p = get_input("int")

                print("Is the attacker aiming for a limb? (1 if yes, 0 if no)")
                l = get_input("int", [0, 1])
                accuracy = 90 - 3 * ea + 1.4 * p + 1.4 * pa - 25 * l
                print("The accuracy check is:")
                print(accuracy)
            elif num == 5:
                print("What is the player's current level?")
                l = get_input("int", [1, 2147483647])
                if l > 1:
                    xp_required = 0.2 * (240 + (l - 1) * (10 + 0.125 * (l - 2)))
                elif l == 1:
                    xp_required = 0.2 * (240)
                print("XP Required:")
                print(int(xp_required))
            elif num == 6:
                if not len(players) == 0:
                    data_choice = str(input("Use saved player data? y/n: "))
                    if data_choice == "n":
                        data_choice = False
                    else:
                        data_choice = True
                else:
                    data_choice = False

                if data_choice:
                    name_recognized = False
                    print("What is the player's name?")
                    while not name_recognized:
                        player_name_choice = get_input("string")
                        for player in players:
                            if player.name == player_name_choice:
                                name_recognized = True
                                player_in_combat = player
                        if not name_recognized:
                            print("That name is not recognized. Try again.")

                    print("Is " + player_in_combat.name + " the attacker or the target?")
                    print("1. Attacker")
                    print("2. Target")
                    it_choice = get_input("int", [1, 2])

                    # When player is attacker
                    if it_choice == 1:
                        a = player_in_combat.get_stat("Dexterity")
                        s = player_in_combat.get_stat("Strength")

                        print("What is the target's dexterity?")
                        ea = get_input("int")
                        print("What is the target's strength?")
                        es = get_input("int")

                    # When player is target
                    elif it_choice == 2:
                        ea = player_in_combat.get_stat("Dexterity")
                        es = player_in_combat.get_stat("Strength")

                        print("What is the attacker's dexterity?")
                        a = get_input("int")
                        print("What is the attacker's strength?")
                        s = get_input("int")
                else:
                    print("What is the attacker's dexterity?")
                    a = get_input("int")
                    print("What is the attacker's strength?")
                    s = get_input("int")
                    print("What is the target's dexterity?")
                    ea = get_input("int")
                    print("What is the target's strength?")
                    es = get_input("int")

                print("What is the modifier?")
                x = get_input("int")
                block_chance = 50 + (3 * a + 2 * s) - (3 * ea + 2 * es) + random.randint(-10, 10) + x
                print("The chance to block is:")
                print(int(block_chance))
            elif num == 7:
                if not len(players) == 0:
                    data_choice = str(input("Use saved player data? y/n: "))
                    if data_choice == "n":
                        data_choice = False
                    else:
                        data_choice = True
                else:
                    data_choice = False

                if data_choice:
                    name_recognized = False
                    print("What is the player's name?")
                    while not name_recognized:
                        player_name_choice = get_input("string")
                        for player in players:
                            if player.name == player_name_choice:
                                name_recognized = True
                                player_in_combat = player
                        if not name_recognized:
                            print("That name is not recognized. Try again.")

                    # Player is attacker
                    c = player_in_combat.get_stat("Charisma")

                    print("What is the " + player_in_combat.name + "'s remaining health?")
                    hr = get_input("int", [1, 2147483647])
                    print("What is " + player_in_combat.name + "'s level?")
                    l = get_input("int", [1, 2147483647])
                else:
                    print("What is the attacker's charisma?")
                    c = get_input("int")
                    print("What is the attacker's remaining health?")
                    hr = get_input("int", [1, 2147483647])
                    print("What is the attacker's level?")
                    l = get_input("int", [1, 2147483647])

                print("What is the target's charisma?")
                ec = get_input("int")
                print("What is the target's endurance?")
                ee = get_input("int")
                print("What is the target's remaining health?")
                ehr = get_input("int", [1, 2147483647])
                print("What is the target's enemy level?")
                el = get_input("int", [1, 2147483647])
                enemy_surrender = ec + ee + ehr + el + random.randint(0, 9)
                player_surrender = c + hr + l + random.randint(0, 9)
                print("The player surrender is: " + str(player_surrender))
                print("The enemy surrender is: " + str(enemy_surrender))
            elif num == 8:
                print("What is the attacker's sneak skill?")
                i = get_input("int")
                print("What is the attacker's armor weight (in kilograms)?")
                w = get_input("float", [0.0, 1000000.0])
                print("What is the target's perception?")
                p = get_input("int")
                print("What is the status of the target?")
                print("1. Aware")
                print("2. Tired")
                print("3. Sleeping")
                status = get_input("int", [1, 3])
                if status == 2:
                    p = p * (2 / 3)
                elif status == 3:
                    p = p * (1 / 10)
                print("Distance between attacker and target?")
                m = get_input("int", [0, 2147483647])
                print("What is the floor sound type?")
                f = get_input("int")
                sneak_chance = 60 + 0.75 * i - 2 * w - 4.5 * p + 2 * m + 9 * f
                print("Sneak Chance: " + str(sneak_chance))
            elif num == 9:
                print("What is the player's Strength?")
                strength = get_input("int")
                print("What is the player's Perception?")
                perception = get_input("int")
                print("What is the player's Endurance?")
                endurance = get_input("int")
                print("What is the player's Charisma?")
                charisma = get_input("int")
                print("What is the player's Dexterity?")
                dexterity = get_input("int")
                print("What is the player's Intelligence?")
                intelligence = get_input("int")
                print("What is the player's Attunement?")
                attunement = get_input("int")

                sneak = dexterity * 3
                lockpicking = intelligence + perception + dexterity
                survival = endurance * 2 + intelligence
                medicine = perception * 2 + intelligence * 2
                pickpocketing = dexterity * 3
                throwing = dexterity + perception + strength
                fishing = perception * 2 + intelligence

                alchemy = intelligence * 2 + attunement
                enchanting = intelligence + attunement * 2
                crafting = intelligence * 2 + perception
                engineering = intelligence * 2
                cooking = intelligence + perception

                print("Sneak: " + str(sneak))
                print("Lockpicking: " + str(lockpicking))
                print("Survival: " + str(survival))
                print("Medicine: " + str(medicine))
                print("Pickpocketing: " + str(pickpocketing))
                print("Throwing: " + str(throwing))
                print("Fishing: " + str(fishing))
                print()
                print("Alchemy: " + str(alchemy))
                print("Enchanting: " + str(enchanting))
                print("Crafting: " + str(crafting))
                print("Engineering: " + str(engineering))
                print("Cooking: " + str(cooking))

            elif num == 10:
                if not established_soul_shard_vars:
                    print("What is the current soul shard chance?")
                    original_soul_shard_chance = get_input("float")
                    soul_shard_chance = original_soul_shard_chance
                    established_soul_shard_vars = True

                rand_num = random.uniform(0, 1)

                print()
                print("Current Soul Shard Chance: " + str(round(soul_shard_chance * 100, 2)) + "%")
                print("Roll: " + str(round(rand_num * 100, 2)))
                print()
                if rand_num <= soul_shard_chance:
                    soul_shard_drop = True
                    original_soul_shard_chance = set_original_soul_shard_chance
                    soul_shard_chance = set_original_soul_shard_chance
                else:
                    soul_shard_drop = False
                    soul_shard_chance += soul_shard_chance_increase
                print("New Soul Shard Chance: " + str(round(soul_shard_chance * 100, 2)) + "%")
                print()
                if soul_shard_drop:
                    print("SOUL SHARD HAS BEEN DROPPED!")
                else:
                    print("No soul shard has been dropped.")

            elif num == 11:
                print("What are you contesting for?")
                print("1. Ranged Weapon")
                print("2. One-Handed Weapon")
                print("3. Two-Handed Weapon")
                contest_weapon = get_input("int", [1, 3])

                if not len(players) == 0:
                    data_choice = str(input("Use saved player data? y/n: "))
                    if data_choice == "n":
                        data_choice = False
                    else:
                        data_choice = True
                else:
                    data_choice = False

                if data_choice:
                    name_recognized = False
                    print("What is the player's name?")
                    while not name_recognized:
                        player_name_choice = get_input("string")
                        for player in players:
                            if player.name == player_name_choice:
                                name_recognized = True
                                player_in_combat = player
                        if not name_recognized:
                            print("That name is not recognized. Try again.")

                    print("Is " + player_in_combat.name + " the attacker or the target?")
                    print("1. Attacker")
                    print("2. Target")
                    it_choice = get_input("int", [1, 2])

                    # When player is attacker
                    if it_choice == 1:
                        s = player_in_combat.get_stat("Strength")
                        a = player_in_combat.get_stat("Dexterity")

                        print("Target strength?")
                        ts = get_input("int")
                        print("Target dexterity?")
                        ta = get_input("int")

                    # When player is target
                    elif it_choice == 2:
                        ts = player_in_combat.get_stat("Strength")
                        ta = player_in_combat.get_stat("Dexterity")

                        print("Attacker strength?")
                        s = get_input("int")
                        print("Attacker dexterity?")
                        a = get_input("int")
                else:
                    print("Attacker strength?")
                    s = get_input("int")
                    print("Attacker dexterity?")
                    a = get_input("int")
                    print("Target strength?")
                    ts = get_input("int")
                    print("Target dexterity?")
                    ta = get_input("int")

                a_modifier = str(s + a)
                t_modifier = str(ts + ta)

                if contest_weapon == 1:  # Ranged
                    print("1d10 + " + a_modifier + " >= 1d8 + " + t_modifier)
                elif contest_weapon == 2:  # One-Handed Weapon
                    print(a_modifier + " >= 1d6 + " + t_modifier)
                elif contest_weapon == 3:  # Two-Handed Weapon
                    print(a_modifier + " >= 1d10 + " + t_modifier)

            elif num == 12:
                access_calculations = False
            print("-----------------------------------")







