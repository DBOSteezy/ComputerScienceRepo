# Devlin O'Rourke
# Intro to Computer Science
# Assignment 8 - Adventure Module (Project)
# 3/9/25

# game.py
from gamefunctions import print_welcome, print_shop_menu, purchase_item, new_random_monster

def main():
    # Get player's name
    player_name = input("Enter your name: ")
    print_welcome(player_name)

    # Show shop menu
    print_shop_menu("Sword", 50.00, "Shield", 30.00)

    # Purchase an item
    money = 100  # Starting money for the player
    item_price = 50.00  # Price of the item
    quantity = 1  # Default quantity
    num_purchased, remaining_money = purchase_item(item_price, money, quantity)
    print(f"You purchased {num_purchased} item(s). Money left: ${remaining_money:.2f}")

    # Spawn a random monster
    monster = new_random_monster()
    print(f"A wild {monster['name']} appears!")
    print(monster['description'])

if __name__ == "__main__":
    main()
