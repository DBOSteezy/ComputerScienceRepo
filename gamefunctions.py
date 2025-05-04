# Devlin O'Rourke
# Intro to Compuer Science
# Assignment 9 - Game Loops
# 3/4/25

"""Game Functions Module

This module contains functions for an adventure game, including purchasing
items, spawning random monsters, printing a welcome message, and showing a
shop menu. these functions can be used to create an interactive text-based
game.

Functions:
    purchase_item(itemPrice: float, startingMoney: float, quantityToPurchase: int = 1 -> tuple:
        Allows a player to purchase items within the game.

    new_random_monster() -> dict:
        Spawns a new random monster with attributes like name, health
        power, and money

    print_welcome(name:str, width: int = 20) -> None:
        Prints a greeting message to the player.

    print_shop_menu(item1Name: str, item1Price: float, item2Name: str, item2Price: float) -> None:
        Displays the shop menu with available items and their prices
"""

import random

def purchase_item(itemPrice: float, startingMoney: float, quantityToPurchase: int = 1):
    """Allows a player to purchase items within the game.

    Parameters:
        itemPrice (float): The price of the item to purchase.
        startingMoney (float): The amount of money the player has.
        quantityToPurchase (int): The number of items the player wants to buy.

    Returns:
        tuple: A tuple containing the number of items purchased and the
        remaining money.
    """

    if startingMoney < itemPrice:
        return 0, startingMoney

    max_affordable = startingMoney // itemPrice
    quantity_purchased = min(max_affordable, quantityToPurchase)
    remaining_money = startingMoney - (quantity_purchased * itemPrice)

    return quantity_purchased, remaining_money

def new_random_monster() -> dict:
    """Spawns a new random monster with attributes

    Returns:
        dict: A dictionary containing the monster's name, description,
        health, power, and money.
    """
    monster_names = ["goblin", "vulture", "dragon"]
    descriptions = {
        "goblin": "This lone goblin. When it notices you, it rushes \
at you quickly, foaming at the mouth and making odd noises. A battle \
cry perhaps? It'python game.py",
        "vulture": "You discover a vulture eating the remains of two orcs \
that appear to be long dead. The vulture cranes its neck up to you and \
coughs.",
        "dragon": "A fearsome dragon with scales that shimmer in the light, \
guarding its treasure. You creep up to its side, then notice its eyes have \
been following you the whole time!"
    }

    health_range = {
        "goblin": (5, 10),
        "vulture": (1, 2),
        "dragon": (5, 10)
    }

    power_range = {
        "goblin": (1, 3),
        "vulture": (0, 1),
        "dragon": (5, 10)
    }

    money_range = {
        "goblin": (1, 3),
        "vulture": (0, 1),
        "dragon": (5, 10)
    }

    name = random.choice(monster_names)
    health = random.randint(*health_range[name])
    power = random.randint(*power_range[name])
    money = round(random.uniform(*money_range[name]), 2)

    return {
        'name': name,
        'description': descriptions[name],
        'health': health,
        'power': power,
        'money': money
    }

def print_welcome(name: str, width:int = 20) -> None:
    """prints a greeting message to the player.

    Parameters:
        name (str): The name of the player.
        width (int): The width for formatting the greeting.

    Returns:
        None
    """
    print(f"{'Hello, ' + name + '!':^{width}}")

def print_shop_menu(item1Name: str, item1Price: float, item2Name: str, item2Price: float) -> None:
    """Displays the shop menu with available items and their prices.

    Parameters:
        item1Name (str): The name of the first item.
        item1Price (float): The price of the first item.
        item2Name (str): The name of the second item.
        item2Price (float): The price of the second item.

    Returns:
        None
    """
    print("/----------------------\\")
    print(f"| {item1Name:<12} ${item1Price:>7.2f} |")
    print(f"| {item2Name:<12} ${item2Price:>7.2f} |")
    print("\\----------------------/")

def get_user_choice(prompt: str, options: list):
    """Prompt user until they enter a valid choice."""
    while True:
        choice = input(prompt).strip()
        if choice in options:
            return choice
        else:
            print(f"Invalid input, please choose from {', '.join(options)}.")

def fight_monster(player_hp, player_gold, monster):
    """Fighting a monster mechanics"""
    print(f"\nA wild {monster['name']} appears!")
    print(monster['description'])
    monster_hp = monster['health']
    while monster_hp > 0 and player_hp > 0:
        print(f"\nYour HP:{player_hp} | {monster['name']} HP:{monster_hp}")
        action = get_user_choice("Do you want to (F)ight or (R)un?", ['F', 'R', 'f', 'r'])
        if action == 'r' or action == 'R':
            print("You run away.")
        elif action == 'f' or action == 'F':
            print("You choose to fight")
            damage_to_monster = random.randint(1, 5)
            damage_to_player = random.randint(0, monster['power'])
            monster_hp -= damage_to_monster
            player_hp -= damage_to_player
            print(f"You deal {damage_to_monster} damage!")
            print(f"{monster['name']} dealt {damage_to_player} damage!")
        else:
            print("Please (F)ight or (R)un")
    if monster_hp <= 0:
        print(f"You defeated the {monster['name']}!")
        print("You've discovered the monsters stash of treasure!")
        player_gold += monster['money']
    elif player_hp <= 0:
        print("You have been defeated......")
    return player_hp, player_gold

# def test_functions():
#    """Function to test the functionalities of the game."""
#    # Test purchase_item function
#    num_purchased, leftover_money = purchase_item(1.23, 10, 3)
#    print(f"Purchased: {num_purchased}, Money left: {leftover_money:.2f}")
#
#    num_purchased, leftover_money = purchase_item(1.23, 10, 3)
#    print(f"Purchased: {num_purchased}, Money left: {leftover_money:.2f}")
#
#    num_purchased, leftover_money = purchase_item(1.23, 10, 3)
#    print(f"Purchased: {num_purchased}, Money left: {leftover_money:.2f}")
#
#    num_purchased, leftover_money = purchase_item(1.23, 10, 3)
#    print(f"Purchased: {num_purchased}, Money left: {leftover_money:.2f}")
#
    # Test new_random_monster function
#    for _ in range(3):
#        my_monster = new_random_monster()
#        print(f"Monster Name: {my_monster['name']}")
#        print(f"Description: {my_monster['description']}")
#        print(f"Health: {my_monster['health']}")
#        print(f"Power: {my_monster['power']}")
#        print(f"Money: {my_monster['money']}")
#
    # Test print_welcome function
#    print_welcome("Jeffery")
#    print_welcome("Audrey")
#    print_welcome("Lord Farquad")

    # Test print_shop_menu function
#    print_shop_menu("Apple", 31, "Pear", 1.234)
#    print_shop_menu("Egg", 1.64, "Bag of Oats", 12.34)
#    print_shop_menu("Orange", 1.5, "Banana", 1.99)

# if __name__ == "__main__":
#    test_functions()
