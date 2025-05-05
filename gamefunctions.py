# Devlin O'Rourke
# Intro to Compuer Science
# Assignment 11 - Saving and Loading
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

    print_welcome(name, width = 20) -> None:
        Prints a greeting message to the player.

    print_shop_menu(item1Name: str, item1Price: float, item2Name: str, item2Price: float) -> None:
        Displays the shop menu with available items and their prices
"""

import random
import json
import os


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

    return int(quantity_purchased), remaining_money

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

def fight_monster(player_hp, player_gold, monster, inventory, equipped_weapon):
    """Fighting a monster mechanics with special item handling."""
    print(f"\nA wild {monster['name']} appears!")
    print(monster['description'])
    monster_hp = monster['health']
    # Check if player has Monster Eliminator
    monster_elim = None
    for item in inventory:
        if item['name'] == 'Monster Eliminator':
            monster_elim = item
            break

    while monster_hp > 0 and player_hp > 0:
        print(f"\nYour HP:{player_hp} | {monster['name']} HP:{monster_hp}")
        action = get_user_choice("Do you want to (F)ight, (R)un, or (U)se item?", ['F','R','U','f','r','u'])
        if action.lower() == 'r':
            print("You run away.")
            break
        elif action.lower() == 'u':
            # Use an item
            used_item = use_item(inventory)
            if used_item:
                if used_item['name'] == 'Monster Eliminator':
                    # Instant kill
                    monster_hp = 0
                    print("Monster Eliminator used! Monster is instantly defeated.")
                    inventory.remove(used_item)
                elif used_item['name'] == 'Health Potion':
                    # Restore health
                    player_hp += 10
                    if player_hp > 30:
                        player_hp = 30
                    print("Health Potion used! Restored 10 HP.")
                    inventory.remove(used_item)
                else:
                    print("Cannot use this item now.")
            continue
        elif action.lower() == 'f':
            print("You choose to fight")
            # Calculate attack damage
            attack_damage = 1
            if equipped_weapon:
                attack_damage = equipped_weapon.get('attack', 1)
                # Decrease durability
                equipped_weapon['currentDurability'] -= 1
                if equipped_weapon['currentDurability'] <= 0:
                    print(f"Your {equipped_weapon['name']} has broken!")
                    inventory.remove(equipped_weapon)
                    equipped_weapon = None
            damage_to_monster = attack_damage + random.randint(0, 2)
            damage_to_player = random.randint(0, monster['power'])
            monster_hp -= damage_to_monster
            player_hp -= damage_to_player
            print(f"You deal {damage_to_monster} damage!")
            print(f"{monster['name']} dealt {damage_to_player} damage!")
            if monster_hp <= 0:
                print(f"You defeated the {monster['name']}!")
                print("You've discovered the monsters stash of treasure!")
                player_gold += monster['money']
            if player_hp <= 0:
                print("You have been defeated......")
                break
    return player_hp, player_gold, inventory, equipped_weapon

def add_item_to_inventory(inventory: list, item:dict):
    """Add an item dictionary to the inventory list."""
    inventory.append(item)
    print(f"Added {item['name']} to inventory.")

def equip_item(inventory: list, item_type: str, current_equipped=None):
    """Lets a user select and equip a piece of equipment."""
    relevant_items = [item for item in inventory if item['type'] == item_type]
    if not relevant_items:
        print(f"No {item_type} found in inventory.")
        return current_equipped
    print(f"Select a {item_type} to equip:")
    for i, item in enumerate(relevant_items, 1):
        if item['type'] == 'weapon':
            print(f"{i}. {item['name']} (Attack: {item.get('attack', 1)}) (Durability: {item['currentDurability']})")
        else:
            print(f"{i}. {item['name']} (Type: {item['type']})")
    choice = get_user_choice(f"Enter number (1-{len(relevant_items)}), or 0 for none: ", [str(i) for i in range(0, len(relevant_items)+1)])
    choice_idx = int(choice)-1
    if choice_idx >=0:
        selected_item = relevant_items[choice_idx]
        print(f"You have equipped {selected_item['name']}!")
        return selected_item
    else:
        print("No item equipped.")
        return None
    
def use_item(inventory: list):
    """Allows player to select a consumable item to use."""
    consumables = [item for item in inventory if item['type'] == 'consumable']
    if not consumables:
        print("No consumable items to use.")
        return None
    print("Consumable items:")
    for i, item in enumerate(consumables, 1):
        print(f"{i}. {item['name']} - {item.get('note', '')}")
    choice = get_user_choice(f"Enter number (1-{len(consumables)}), or 0 to cancel: ", [str(i) for i in range(0, len(consumables)+1)])
    choice_idx = int(choice)-1
    if choice_idx >= 0:
        selected = consumables[choice_idx]
        return selected
    else:
        return None

def save_game(filename, inventory, player_hp, player_gold):
    """
    Save the current game state to a JSON file.

    Args:
        filename (str): The filename to save the game to.
        inventory (list): List of item dictionaries in the player's inventory.
        player_hp (int): The player's current health points.
        player_gold (int): The player's current gold.
    """
    game_state = {
        'inventory': inventory,
        'player_hp': player_hp,
        'player_gold': player_gold
    }
    try:
        with open(filename, 'w') as f:
            json.dump(game_state, f)
        print("Game saved successfully.")
    except Exception as e:
        print(f"Error saving game: {e}")

def load_game(filename):
    """
    Load the game state from a JSON file.

    Args:
        filename (str): The filename to load the game from.

    Returns:
        tuple: (inventory, player_hp, player_gold)
    """
    try:
        with open(filename, 'r') as f:
            game_state = json.load(f)
        inventory = game_state.get('inventory', [])
        player_hp = game_state.get('player_hp', 30)
        player_gold = game_state.get('player_gold', 0)
        print("Game loaded successfully.")
        return inventory, player_hp, player_gold
    except FileNotFoundError:
        print("Save file not found. Starting a new game.")
        return [], 30, 0
    except json.JSONDecodeError:
        print("Corrupted save file. Starting a new game.")
        return [], 30, 0
    except Exception as e:
        print(f"Error loading game: {e}")
        return [], 30, 0
