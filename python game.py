
# Devlin O'Rourke
# Intro to Computer Science
# Assignment 9 - Game Loops
# 5/4/25

# game.py
from gamefunctions import (
    print_welcome,
    print_shop_menu,
    purchase_item,
    new_random_monster,
    fight_monster,
    get_user_choice
)

def main():
    # Get player's name
    player_name = input("Enter your name: ")
    print_welcome(player_name)
    player_hp = 30
    player_gold = 10

    # Main game loop
    while True:
        print("\nYou are in your home village.")
        print(f"Current HP:{player_hp} | Current Gold:{player_gold}")
        print("What would you like to do?")
        print("1. Leave town (Fight Monster)")
        print("2. Sleep (Restore HP for 5 Gold)")
        print("3. Quit")
        choice = get_user_choice("Enter your choice (1-3): ", ['1', '2', '3'])

        if choice == '1':
            # Fight a monster
            monster = new_random_monster()
            player_hp, player_gold = fight_monster(player_hp, player_gold, monster)
            if player_hp <= 0:
                print("You died and have left these lands to ruin without you.")
                break # Exit game loop
        elif choice == '2':
            # Sleep to restore HP
            sleep_cost = 5
            if player_gold >= sleep_cost:
                player_gold -= sleep_cost
                player_hp = 30
                print("You slept well and feel great.")
            else:
                print("Aint no rest for the wicked, or the poor in this case.")
        elif choice == '3':
            print("Thanks for playing!")
            break # Exit game

    # Show shop menu
#    print_shop_menu("Sword", 50.00, "Shield", 30.00)

    # Purchase an item
#    money = 100 # Starting money for the player
#    item_price = 50.00 # Price of the item
#    quantity = 1 # Default quantity
#    num_purchased, remaining_money = purchase_item(item_price, money, quantity)
#    print(f"You purchased {num_purchased} item(s). Money left: ${remaining_money:.2f}")

    # Spawn a random monster
#    monster = new_random_monster()
#    print(f"A wild{monster['name']} appears!")
#    print(monster['description'])

if __name__ == "__main__":
    main()

