from Globals import *


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