# Devlin O'Rourke
# Intro to Computer Science
# Assignment 5 - Adventure Functions (Project)
# 2/11/25


"""Game Functions Module.

This module contains functions for an adventure game, including purchasing
items, spawning random monsters, printing a welcome message, and showing a
shop menu. These functions can be used to create an interactive text-based
game.

Functions:
    purchase_item(itemPrice: float, startingMoney: float, quantityToPurchase: int = 1) -> tuple:
        Allows a player to purchase items within the game.
    
    new_random_monster() -> dict:
        Spawns a new random monster with attributes like name, health,
        power, and money.
    
    print_welcome(name: str, width: int = 20) -> None:
        Prints a greeting message to the player.
    
    print_shop_menu(item1Name: str, item1Price: float, item2Name: str, item2Price: float) -> None:
        Displays the shop menu with available items and their prices.
"""

import random

def purchase_item(itemPrice: float, startingMoney: float, quantityToPurchase: int = 1) -> tuple:
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
    """Spawns a new random monster with attributes.

    Returns:
        dict: A dictionary containing the monster's name, description,
        health, power, and money.
    """
    monster_names = ["A goblin", "A vulture", "A dragon"]
    descriptions = {
        "A goblin": "This is a lone goblin. When it notices you, it rushes \
at you quickly with a sharp dagger drawn.",
        "A vulture": "You discover a vulture eating the remains of two orcs \
that appear to have killed each other.",
        "A dragon": "A fearsome dragon with scales that shimmer in the light, \
guarding its treasure."
    }

    health_range = {
        "A goblin": (5, 10),
        "A vulture": (0, 1),
        "A dragon": (20, 40)
    }

    power_range = {
        "A goblin": (1, 3),
        "A vulture": (0, 1),
        "A dragon": (5, 10)
    }

    money_range = {
        "A goblin": (1, 3),
        "A vulture": (0, 1),
        "A dragon": (5, 10)
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

def print_welcome(name: str, width: int = 20) -> None:
    """Prints a greeting message to the player.

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

def test_functions():
    """Function to test the functionalities of the game functions."""
    # Test purchase_item function
    num_purchased, leftover_money = purchase_item(1.23, 10, 3)
    print(f"Purchased: {num_purchased}, Money left: {leftover_money:.2f}")

    num_purchased, leftover_money = purchase_item(1.23, 2.01, 3)
    print(f"Purchased: {num_purchased}, Money left: {leftover_money:.2f}")

    num_purchased, leftover_money = purchase_item(3.41, 21.12)
    print(f"Purchased: {num_purchased}, Money left: {leftover_money:.2f}")

    num_purchased, leftover_money = purchase_item(40, 20)
    print(f"Purchased: {num_purchased}, Money left: {leftover_money:.2f}")

    # Test new_random_monster function
    for _ in range(3):
        my_monster = new_random_monster()
        print(f"Monster Name: {my_monster['name']}")
        print(f"Description: {my_monster['description']}")
        print(f"Health: {my_monster['health']}")
        print(f"Power: {my_monster['power']}")
        print(f"Money: {my_monster['money']}")

    # Test print_welcome function
    print_welcome("Jeffery")
    print_welcome("Audrey")
    print_welcome("Ingridey")

    # Test print_shop_menu function
    print_shop_menu("Apple", 31, "Pear", 1.234)
    print_shop_menu("Egg", 1.64, "Bag of Oats", 12.34)
    print_shop_menu("Orange", 1.5, "Banana", 1.99)

if __name__ == "__main__":
    test_functions()
