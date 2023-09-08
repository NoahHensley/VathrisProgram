import random


def get_input(type = "string", range = None):
    if range == None:
        if type == "int":
            range = [-2147483648, 2147483647]
        elif type == "float":
            range = [-1000000.0, 1000000.0]
    while True:
        try:
            if type == "string":
                choice = str(input())
            elif type == "int":
                choice = int(input())
                if not range[0] <= choice <= range[1]:
                    raise Exception
            elif type == "float":
                choice = float(input())
                if not range[0] <= choice <= range[1]:
                    raise Exception
            return choice
        except Exception:
            if type == "string":
                print("You must enter a string.")
            elif type == "int":
                print("You must enter an int between " + str(range[0]) + " and " + str(range[1]) + ".")
            elif type == "float":
                print("You must enter a float between " + str(range[0]) + " and " + str(range[1]) + ".")


class Player:
    def __init__(self):
        self.inventory = []
        self.total_mass = 0

        self.stats = [
            ["Strength", 0],
            ["Perception", 0],
            ["Endurance", 0],
            ["Charisma", 0],
            ["Dexterity", 0],
            ["Intelligence", 0],
            ["Attunement", 0]
        ]
        self.size = 0

        print("What is the player's name?")
        self.name = get_input("string")

        for i in range(len(self.stats)):
            print("What is " + self.name + "'s " + self.stats[i][0] + "?")
            self.stats[i][1] = get_input("int", [0, 2147483647])

        print("What is " + self.name + "'s size (square area number)?")
        self.size = get_input("int")

        print("How many coins does " + self.name + " have?")
        self.coins = get_input("int", [0, 2147483647])

        print("Enter all of the items that " + self.name + " has.")
        finished = False
        while not finished:
            self.inventory.append(Player.get_item_info())

            choice = str(input("Finished? y/n: "))
            if choice == "y":
                finished = True

        self.calculate_total_mass()

    def get_stat(self, stat_input):
        for stat in self.stats:
            if stat[0] == stat_input:
                return stat[1]

    @staticmethod
    def get_item_info():
        item_name = str(input("Name: "))
        while True:
            try:
                item_mass = float(input("Mass: "))
                break
            except Exception:
                print("You must enter a float.")
        while True:
            try:
                item_quantity = int(input("Quantity: "))
                break
            except Exception:
                print("You must enter an int.")
        return [item_name, item_mass, item_quantity]

    def calculate_total_mass(self):
        self.total_mass = 0
        for item in self.inventory:
            self.total_mass += item[1] * item[2]


class Enemy:
    def __init__(self, nameInput, levelInput, healthInput, dropsInput, coinsDropInput):
        self.name = nameInput
        self.level = levelInput
        self.maxHealth = healthInput
        self.drops = dropsInput
        self.coins = coinsDropInput

        drops_removing = []
        for drop in self.drops:
            if drop[2] == 0:
                drops_removing.append(drop)
        for drop in drops_removing:
            self.drops.remove(drop)

    @staticmethod
    def calculate_potential_drops(potential_drops):
        drops_removing = []
        for drop in potential_drops:
            rand_num = random.uniform(0, 1)
            if rand_num > drop[2]:
                drops_removing.append(drop)
        for drop in drops_removing:
            potential_drops.remove(drop)
        return potential_drops

    def print_info(self):
        print(self.name)
        print("Level: " + str(self.level))
        print("Health: " + str(self.maxHealth))
        print(self.drops)
        print("Coins: " + str(self.coins))


class JeranPython(Enemy):
    def __init__(self):
        name = "Jeran Python"
        level = random.randint(1, 2)
        health = 12 + 2 * (level - 1)

        drops = [
            ["Jeran Python Meat", 0.2, random.randint(1, 2)],
            ["Jeran Python Skin", 0.1, 1]
        ]

        potential_drops = Enemy.calculate_potential_drops([
            ["Silverleaf", 0.1, 0.0001],
            ["Kingsfoil", 0.1, 0.0001]
        ])
        for drop in potential_drops:
            drops.append(drop)

        coins_drop = 0

        super().__init__(name, level, health, drops, coins_drop)


class JeranFlawn(Enemy):
    def __init__(self):
        name = "Jeran Flawn"
        level = random.randint(2, 4)
        health = 12 + 2 * (level - 2)

        drops = [
            ["Jeran Flawn Eye", 0.02, 1],
            ["Jeran Flawn Skin", 0.08, 1]
        ]

        potential_drops = Enemy.calculate_potential_drops([
            ["Silverleaf", 0.1, 0.1],
            ["Kingsfoil", 0.1, 0.1]
        ])
        for drop in potential_drops:
            drops.append(drop)

        coins_drop = 0

        super().__init__(name, level, health, drops, coins_drop)


class AgitatedOrangutan(Enemy):
    def __init__(self):
        name = "Agitated Orangutan"
        level = random.randint(1, 2)
        health = 13 + 2 * (level - 2)

        drops = [
            ["Jeran Orangutan Meat", 0.1, random.randint(1, 2)],
            ["Jeran Orangutan Skin", 0.1, 1]
        ]

        potential_drops = Enemy.calculate_potential_drops([
            ["Silverleaf", 0.1, 0.1],
            ["Kingsfoil", 0.1, 0.1]
        ])
        for drop in potential_drops:
            drops.append(drop)

        coins_drop = 0

        super().__init__(name, level, health, drops, coins_drop)


class Faethling(Enemy):
    def __init__(self):
        name = "Faethling"
        level = random.randint(1, 2)
        health = 5 + 2 * (level - 1)

        drops = [
            ["Little Faethling Sword", 0.15, 1],
            ["Faethling Ash", 0.01, random.randint(1, 2)]
        ]

        potential_drops = Enemy.calculate_potential_drops([

        ])
        for drop in potential_drops:
            drops.append(drop)

        coins_drop = 0

        super().__init__(name, level, health, drops, coins_drop)


class TallonArcher(Enemy):
    def __init__(self):
        name = "\"Tallon\" Archer"
        level = random.randint(1, 2)
        health = 13 + 2 * (level - 1)

        drops = [
            ["Weird Tallon Cloth", 0.08, random.randint(0, 2)],
            ["Arrow", 0.1, random.randint(0, 9)]
        ]

        potential_drops = Enemy.calculate_potential_drops([
            ["Weirdly-Shaped Tallon Bow", 2, 0.1],
            ["Weirdly-Shaped Tallon Armor", 4, 0.1]
        ])
        for drop in potential_drops:
            drops.append(drop)

        coins_drop = random.randint(0, 3)

        super().__init__(name, level, health, drops, coins_drop)


class TallonSoldier(Enemy):
    def __init__(self):
        name = "\"Tallon\" Soldier"
        level = random.randint(1, 2)
        health = 15 + 2 * (level - 1)

        drops = [
            ["Weird Tallon Cloth", 0.08, random.randint(0, 2)]
        ]

        potential_drops = Enemy.calculate_potential_drops([
            ["Weirdly-Shaped Tallon Bow", 2, 0.1],
            ["Weirdly-Shaped Tallon Helmet", 1, 0.1],
            ["Weirdly-Shaped Tallon Armor", 4, 0.1]
        ])
        for drop in potential_drops:
            drops.append(drop)

        coins_drop = random.randint(0, 3)

        super().__init__(name, level, health, drops, coins_drop)


class TallonShipCaptain(Enemy):
    def __init__(self):
        name = "\"Tallon\" Ship Captain"
        level = 3
        health = 22

        drops = [
            ["Weird Tallon Cloth", 0.08, random.randint(0, 2)],
            ["Tallon Firebomb", 0.75, random.randint(0, 4)]
        ]
        potential_drops = Enemy.calculate_potential_drops([
            ["Weirdly-Shaped Tallon Captain's Sword", 1.8, 0.1],
            ["Weirdly-Shaped Tallon Captain's Helmet", 0.5, 0.1],
            ["Weirdly-Shaped Tallon Captain's Armor", 4, 0.1]
        ])

        for drop in potential_drops:
            drops.append(drop)

        coins_drop = random.randint(3, 8)

        super().__init__(name, level, health, drops, coins_drop)


class GoblinKnifethrower(Enemy):
    def __init__(self):
        name = "Goblin Knifethrower"
        level = random.randint(1, 2)
        health = 8 + 2 * (level - 1)

        drops = [
            ["Tallon Goblin Knife", 1.2, random.randint(2, 3)],
            ["Goblin Cloth", 0.1, random.randint(0, 2)],
        ]
        potential_drops = Enemy.calculate_potential_drops([
            ["Goblin Knifethrower Vest", 0.7, 0.2],
            ["Weak Molotov Cocktail", 0.5, 0.2]
        ])

        for drop in potential_drops:
            drops.append(drop)

        coins_drop = random.randint(0, 3)

        super().__init__(name, level, health, drops, coins_drop)


class GoblinCamouflager(Enemy):
    def __init__(self):
        name = "Goblin Camouflager"
        level = random.randint(2, 3)
        health = 10 + 2 * (level - 2)

        drops = [
            ["Tallon Goblin Knife", 1.2, random.randint(2, 3)],
            ["Goblin Cloth", 0.1, random.randint(1, 3)],
            ["Recipe for Weak Molotov Cocktail", 0.1, 1]
        ]

        potential_drops = Enemy.calculate_potential_drops([
            ["Goblin Knifethrower Vest", 0.7, 0.2],
            ["Weak Molotov Cocktail", 0.5, 0.2]
        ])
        for drop in potential_drops:
            drops.append(drop)

        coins_drop = random.randint(2, 5)

        super().__init__(name, level, health, drops, coins_drop)


class TallonMage(Enemy):
    def __init__(self):
        name = "\"Tallon\" Mage"
        level = random.randint(2, 3)
        health = 10 + 2 * (level - 1)

        drops = [
            ["Weird Tallon Cloth", 0.08, random.randint(0, 2)]
        ]

        potential_drops = Enemy.calculate_potential_drops([
            ["Tallon Mage Robes", 2, 0.1],
            ["Silverleaf", 0.1, 0.3333],
            ["Kingsfoil", 0.1, 0.3333],
            ["Empty Flask", 0.5, 0.2],
            ["Filled Flask", 0.5, 0.2],
            ["Weak Klyson Potion", 0.15, 0.2],
            ["Weak Health Potion", 0.15, 0.2],
            ["Weak Speed Potion", 0.15, 0.2],
            ["Recipe for Weak Klyson Potion", 0.15, 0.1],
            ["Recipe for Weak Speed Potion", 0.15, 0.1]
        ])
        for drop in potential_drops:
            drops.append(drop)

        coins_drop = random.randint(0, 4)

        super().__init__(name, level, health, drops, coins_drop)


class TallonWarlock(Enemy):
    def __init__(self):
        name = "\"Tallon\" Warlock"
        level = random.randint(2, 3)
        health = 10 + 2 * (level - 1)

        drops = [
            ["Weird Tallon Cloth", 0.08, random.randint(0, 2)]
        ]

        potential_drops = Enemy.calculate_potential_drops([
            ["Tallon Mage Robes", 2, 0.1],
            ["Silverleaf", 0.1, 0.3333],
            ["Kingsfoil", 0.1, 0.3333],
            ["Empty Flask", 0.5, 0.2],
            ["Filled Flask", 0.5, 0.2],
            ["Weak Klyson Potion", 0.15, 0.2],
            ["Weak Health Potion", 0.15, 0.2],
            ["Weak Speed Potion", 0.15, 0.2],
            ["Recipe for Weak Klyson Potion", 0.15, 0.1],
            ["Recipe for Weak Speed Potion", 0.15, 0.1]
        ])
        for drop in potential_drops:
            drops.append(drop)

        coins_drop = random.randint(0, 4)

        super().__init__(name, level, health, drops, coins_drop)


class TallonMissionCommander(Enemy):
    def __init__(self):
        name = "\"Tallon\" Mission Commander"
        level = 5
        health = 32

        drops = [
            ["Weird Tallon Cloth", 0.08, random.randint(0, 2)],
            ["Tallon Goblin Knife", 1.2, random.randint(0, 5)]
        ]

        potential_drops = Enemy.calculate_potential_drops([
            ["Tallon Mission Commander Helmet", 1.3, 0.1],
            ["Tallon Mission Commander Armor", 3.4, 0.1],
            ["Tallon Mission Commander Sword", 1.8, 0.1]
        ])
        for drop in potential_drops:
            drops.append(drop)

        coins_drop = random.randint(2, 8)

        super().__init__(name, level, health, drops, coins_drop)


class AmbolGuard(Enemy):
    def __init__(self):
        name = "Ambol Guard"
        level = random.randint(2, 3)
        health = 13 + 2 * (level - 2)

        drops = [
            ["Ambol Cloth", 0.1, random.randint(0, 2)]
        ]

        potential_drops = Enemy.calculate_potential_drops([
            ["Standard Ambol Guard Armor", 1.9, 0.1],
            ["Standard Ambol Guard Helmet", 0.9, 0.1],
            ["Standard Ambol Guard Sword", 1.5, 0.1]
        ])
        for drop in potential_drops:
            drops.append(drop)

        coins_drop = random.randint(2, 8)

        super().__init__(name, level, health, drops, coins_drop)


class CommanderFinch(Enemy):
    def __init__(self):
        name = "Commander Finch"
        level = 6
        health = 40

        drops = [
            ["Head of Commander Finch", 4.3, 1],
            ["Ambol Cloth", 0.1, random.randint(1, 3)]
        ]

        rand_equips = [
            ["Helmet of Commander Finch", 1.1, 1],
            ["Armor of Commander Finch", 2.8, 1],
            ["Sword of Commander Finch", 1.4, 1]
        ]
        drops.append(random.choice(rand_equips))

        potential_drops = Enemy.calculate_potential_drops([
            ["Standard Ambol Guard Armor", 1.9, 0.1],
            ["Standard Ambol Guard Helmet", 0.9, 0.1],
            ["Standard Ambol Guard Sword", 1.5, 0.1]
        ])
        for drop in potential_drops:
            drops.append(drop)

        coins_drop = random.randint(4, 8)

        super().__init__(name, level, health, drops, coins_drop)


class CrawlingCod(Enemy):
    def __init__(self):
        name = "Crawling Cod"
        level = random.randint(3, 4)
        health = 12 + 2 * (level - 3)

        drops = [
            ["Raw Crawling Cod", 5, 1]
        ]

        potential_drops = Enemy.calculate_potential_drops([
            ["Jeweled Tideberth Ring", 0.1, 0.05]
        ])
        for drop in potential_drops:
            drops.append(drop)

        coins_drop = 0

        super().__init__(name, level, health, drops, coins_drop)


class TideberthCavernNaga(Enemy):
    def __init__(self):
        name = "Tideberth Cavern Naga"
        level = random.randint(4, 5)
        health = 22 + 2 * (level - 4)

        drops = []

        potential_drops = Enemy.calculate_potential_drops([
            ["Raw Copper", 1, 0.2],
            ["Raw Tin", 1, 0.2],
            ["Raw Iron", 1, 0.2],
            ["Elongated Naga Spear", 1.8, 0.1]
        ])
        for drop in potential_drops:
            drops.append(drop)

        coins_drop = random.randint(6, 8)

        super().__init__(name, level, health, drops, coins_drop)


class TideberthAssassin(Enemy):
    def __init__(self):
        name = "Tideberth Assassin"
        level = random.randint(4, 5)
        health = 20 + 2 * (level - 4)

        drops = []

        potential_drops = Enemy.calculate_potential_drops([
            ["Weak Molotov Cocktail", 0.1, 0.5],
            ["Raw Copper", 1, 0.2],
            ["Raw Tin", 1, 0.2],
            ["Raw Iron", 1, 0.2],
            ["Tideberth Assassin Dagger", 1.1, 0.1],
            ["Recipe for Weak Molotov Cocktail", 0.1, 0.1]
        ])
        for drop in potential_drops:
            drops.append(drop)

        coins_drop = random.randint(6, 8)

        super().__init__(name, level, health, drops, coins_drop)


class TideberthMage(Enemy):
    def __init__(self):
        name = "Tideberth Mage"
        level = random.randint(4, 5)
        health = 18 + 2 * (level - 4)

        drops = []

        potential_drops = Enemy.calculate_potential_drops([
            ["Weak Molotov Cocktail", 0.1, 0.5],
            ["Raw Copper", 1, 0.2],
            ["Raw Tin", 1, 0.2],
            ["Raw Iron", 1, 0.2],
            ["Weak Health Potion", 0.5, 0.2],
            ["Weak Klyson Potion", 0.5, 0.2]
        ])
        for drop in potential_drops:
            drops.append(drop)

        coins_drop = random.randint(6, 8)

        super().__init__(name, level, health, drops, coins_drop)


class TideberthSorcerer(Enemy):
    def __init__(self):
        name = "Tideberth Sorcerer"
        level = random.randint(4, 5)
        health = 18 + 2 * (level - 4)

        drops = []

        potential_drops = Enemy.calculate_potential_drops([
            ["Weak Molotov Cocktail", 0.1, 0.5],
            ["Raw Copper", 1, 0.2],
            ["Raw Tin", 1, 0.2],
            ["Raw Iron", 1, 0.2],
            ["Weak Health Potion", 0.5, 0.2],
            ["Weak Klyson Potion", 0.5, 0.2]
        ])
        for drop in potential_drops:
            drops.append(drop)

        coins_drop = random.randint(6, 8)

        super().__init__(name, level, health, drops, coins_drop)


class TideberthCorrupter(Enemy):
    def __init__(self):
        name = "Tideberth Corrupter"
        level = random.randint(5, 6)
        health = 24 + 2 * (level - 5)

        drops = []

        potential_drops = Enemy.calculate_potential_drops([
            ["Weak Molotov Cocktail", 0.1, 0.5],
            ["Raw Copper", 1, 0.2],
            ["Raw Tin", 1, 0.2],
            ["Raw Iron", 1, 0.2],
            ["Weak Health Potion", 0.5, 0.2],
            ["Weak Klyson Potion", 0.5, 0.2],
            ["Weak Speed Potion", 0.5, 0.2]
        ])
        for drop in potential_drops:
            drops.append(drop)

        coins_drop = random.randint(6, 8)

        super().__init__(name, level, health, drops, coins_drop)


class TideberthCavernMonster(Enemy):
    def __init__(self):
        name = "Tideberth Cavern Monster"
        level = random.randint(4, 5)
        health = 30 + 2 * (level - 4)

        drops = [
            ["Tideberth Stone", 1.3, random.randint(1, 3)]
        ]

        potential_drops = Enemy.calculate_potential_drops([
            ["Raw Copper", 1, 0.2],
            ["Raw Tin", 1, 0.2],
            ["Raw Iron", 1, 0.2]
        ])
        for drop in potential_drops:
            drops.append(drop)

        coins_drop = 0

        super().__init__(name, level, health, drops, coins_drop)


class TideberthWaterElemental(Enemy):
    def __init__(self):
        name = "Tideberth Water Elemental"
        level = random.randint(4, 5)
        health = 22 + 2 * (level - 4)

        drops = [
            ["Tideberth Elemental Copper Brace", 1.5, 2]
        ]

        potential_drops = Enemy.calculate_potential_drops([
            ["Raw Copper", 1, 0.2],
            ["Raw Tin", 1, 0.2],
            ["Raw Iron", 1, 0.2]
        ])
        for drop in potential_drops:
            drops.append(drop)

        coins_drop = 0

        super().__init__(name, level, health, drops, coins_drop)


class TideberthMimic(Enemy):
    def __init__(self):
        name = "Tideberth Mimic"
        level = 5
        health = 50

        drops = [
            ["Pickaxe", 2, 3]
        ]

        potential_drops = Enemy.calculate_potential_drops([
            ["Weak Health Potion", 0.5, 0.3333],
            ["Weak Klyson Potion", 0.5, 0.3333],
            ["Weak Speed Potion", 0.5, 0.3333],
            ["Weak Linen Bandage", 0.3, 0.3333],
            ["Tight Linen Bandage", 0.4, 0.3333],
            ["Raw Copper", 1, 0.3333],
            ["Raw Iron", 1, 0.3333],
            ["Raw Emerald", 1, 0.3333],
            ["Raw Azure", 1, 0.3333],
            ["Raw Amethyst", 1, 0.3333],
            ["Dreamfoil", 0.1, 0.3333],
            ["Green Lotus", 0.1, 0.3333],
            ["Earthroot", 0.1, 0.3333],
            ["Crystalline Lotus", 0.1, 0.3333],
            ["Cavernous Snapping Plant", 0.1, 0.3333]
        ])
        for drop in potential_drops:
            drops.append(drop)

        coins_drop = random.randint(15, 20)

        super().__init__(name, level, health, drops, coins_drop)


class HeadTideberthMagus(Enemy):
    def __init__(self):
        name = "Head Tideberth Magus"
        level = 8
        health = 60

        drops = [
            ["Violet Magus Turban", 0.7, 1]
        ]

        potential_drops = Enemy.calculate_potential_drops([
            ["Raw Copper", 1, 0.2],
            ["Raw Tin", 1, 0.2],
            ["Raw Iron", 1, 0.2],
            ["Weak Health Potion", 0.5, 0.2],
            ["Weak Klyson Potion", 0.5, 0.2],
            ["Weak Speed Potion", 0.5, 0.2]
        ])
        for drop in potential_drops:
            drops.append(drop)

        coins_drop = random.randint(6, 8)

        super().__init__(name, level, health, drops, coins_drop)


class CavernousSnappingPlant(Enemy):
    def __init__(self):
        name = "Cavernous Snapping Plant"
        level = random.randint(3, 4)
        health = 14 + 2 * (level - 3)

        drops = [
            ["Leaf", 0.1, random.randint(2, 3)]
        ]

        potential_drops = Enemy.calculate_potential_drops([])
        for drop in potential_drops:
            drops.append(drop)

        coins_drop = 0

        super().__init__(name, level, health, drops, coins_drop)


class GorsonLion(Enemy):
    def __init__(self):
        name = "Gorson Lion"
        level = random.randint(4, 5)
        health = 22 + 2 * (level - 4)

        drops = [
            ["Gorson Lion Hide", 1.8, random.randint(1, 2)],
            ["Raw Gorson Lion Meat", 1.5, random.randint(1, 2)]
        ]

        potential_drops = Enemy.calculate_potential_drops([])
        for drop in potential_drops:
            drops.append(drop)

        coins_drop = 0

        super().__init__(name, level, health, drops, coins_drop)


class GorsonKodo(Enemy):
    def __init__(self):
        name = "Gorson Kodo"
        level = random.randint(5, 6)
        health = 30 + 2 * (level - 5)

        drops = [
            ["Gorson Kodo Leather", 2.2, random.randint(1, 2)],
            ["Raw Gorson Kodo Meat", 1.8, random.randint(1, 2)]
        ]

        potential_drops = Enemy.calculate_potential_drops([])
        for drop in potential_drops:
            drops.append(drop)

        coins_drop = 0

        super().__init__(name, level, health, drops, coins_drop)


class LargeGorsonAnt(Enemy):
    def __init__(self):
        name = "Large Gorson Ant"
        level = random.randint(4, 5)
        health = 20 + 2 * (level - 4)

        drops = [
            ["Large Gorson Ant Skin", 1.3, random.randint(1, 2)],
            ["Raw Gorson Ant Meat", 1.4, random.randint(1, 2)]
        ]

        potential_drops = Enemy.calculate_potential_drops([])
        for drop in potential_drops:
            drops.append(drop)

        coins_drop = 0

        super().__init__(name, level, health, drops, coins_drop)


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
            print("11. Go Back")
            num = get_input("int", [1, 11])

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
                            agility = player.get_stat("Dexterity")
                            is_player = True
                    if not is_player or not data_choice:
                        print("What is " + sequence_combatants[a] + "'s agility?")
                        agility = get_input("int")
                    ind_sequence = random.uniform(0, 7) + agility
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

                        print("Target agility?")
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
                    print("Target agility?")
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
                    print("How many other targets are in the initiator's line of sight?")
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

                        print("Agility of target?")
                        ea = get_input("int")

                    # When player is target
                    elif it_choice == 2:
                        ea = player_in_combat.get_stat("Dexterity")

                        print("Agility of attacker?")
                        pa = get_input("int")
                        print("Perception of attacker?")
                        p = get_input("int")
                else:
                    print("Agility of target?")
                    ea = get_input("int")
                    print("Agility of attacker?")
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

                        print("What is the target's agility?")
                        ea = get_input("int")
                        print("What is the target's strength?")
                        es = get_input("int")

                    # When player is target
                    elif it_choice == 2:
                        ea = player_in_combat.get_stat("Dexterity")
                        es = player_in_combat.get_stat("Strength")

                        print("What is the attacker's agility?")
                        a = get_input("int")
                        print("What is the attacker's strength?")
                        s = get_input("int")
                else:
                    print("What is the attacker's agility?")
                    a = get_input("int")
                    print("What is the attacker's strength?")
                    s = get_input("int")
                    print("What is the target's agility?")
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
                print("What is the player's Agility?")
                agility = get_input("int")
                print("What is the player's Intelligence?")
                intelligence = get_input("int")
                print("What is the player's Attunement?")
                attunement = get_input("int")

                sneak = agility * 3
                lockpicking = intelligence + perception + agility
                survival = endurance * 2 + intelligence
                medicine = perception * 2 + intelligence * 2
                pickpocketing = agility * 3
                throwing = agility + perception + strength
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

            elif num == -1337:
                print("What are you contesting for?")
                print("1. Ranged Weapon")
                print("2. One-Handed Weapon")
                print("3. Two-Handed Weapon")
                contest_weapon = get_input("int", [1, 3])

                if contest_weapon == 1:
                    pass

            elif num == 11:
                access_calculations = False
            print("-----------------------------------")







