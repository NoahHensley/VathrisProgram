import random


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

    def print_info(self, quantity = 1):
        print(self.name + " (" + str(quantity) + ")")
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