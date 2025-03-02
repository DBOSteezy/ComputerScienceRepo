# Devlin O'Rourke
# Intro to Computer Science
# Assignment 5 - Adventure Functions (Project)
# 2/11/25


# All imports
import random

# Allows you to purchase in game items
def purchase_item(itemPrice: float, startingMoney: float, quantityToPurchase: int = 1):
    '''Creates a purchase function to be developed further and used in the game'''
    if startingMoney < itemPrice:
        return 0, startingMoney

    max_affordable = startingMoney // itemPrice
    quantity_purchased = min(max_affordable, quantityToPurchase)
    remaining_money = startingMoney - (quantity_purchased * itemPrice)

    return quantity_purchased, remaining_money

# Spawns a new random monster
def new_random_monster():
    ''' Creates a function to spawn random monsters'''
    monster_names = ["A goblin", "A vulture", "A dragon"]
    descriptions = {"A goblin": "This is a lone goblin. When it notices you, it rushes at you quickly with a sharp dagger drawn.",
                    "A vulture": "You discover a vulture eating the remains of two orcs that appear to have killed each other.",
                    "A dragon": "A fearsome dragon with scales that shimmer in the light, guarding its treasure."
    }

# Start available monsters
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
# End available monsters

# 
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
my_monster = new_random_monster()
print(f"Monster Name: {my_monster['name']}")
print(f"Description: {my_monster['description']}")
print(f"Health: {my_monster['health']}")
print(f"Power: {my_monster['health']}")
print(f"Money: {my_monster['money']}")

my_monster = new_random_monster()
print(f"Monster Name: {my_monster['name']}")
print(f"Description: {my_monster['description']}")
print(f"Health: {my_monster['health']}")
print(f"Power: {my_monster['health']}")
print(f"Money: {my_monster['money']}")

my_monster = new_random_monster()
print(f"Monster Name: {my_monster['name']}")
print(f"Description: {my_monster['description']}")
print(f"Health: {my_monster['health']}")
print(f"Power: {my_monster['health']}")
print(f"Money: {my_monster['money']}")

# Assignment 6 addition
# Delete this comment after turning in

# Prints a welcome message for player
def print_welcome(name: str, width: int = 20):
    '''Prints a greeting to the player'''
    print(f"{'Hello, ' + name + '!':^{width}}")

# Testing print_welcome function
print_welcome("Jeffery")
print_welcome("Audrey")
print_welcome("Ingridey")

# Prints the shop menu
def print_shop_menu(item1Name: str, item1Price: float, item2Name: str, item2Price: float):
    '''Creates a shop item menu. To be developed further'''
    print("/----------------------\\")
    print(f"| {item1Name:<12} ${item1Price:>7.2f} |")
    print(f"| {item2Name:<12} ${item2Price:>7.2f} |")
    print("\\----------------------/")

# Test print_shop_menu function
print_shop_menu("Apple", 31, "Pear", 1.234)
print_shop_menu("Egg", 1.64, "Bag of Oats", 12.34)
print_shop_menu("Orange", 1.5, "Banana", 1.99)






