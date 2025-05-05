
# Devlin O'Rourke
# Intro to Computer Science
# Assignment 10 - Inventory List
# 5/4/25

# game.py
from gamefunctions import (
    print_welcome,
    print_shop_menu,
    purchase_item,
    new_random_monster,
    fight_monster,
    get_user_choice,
    add_item_to_inventory,
    equip_item,
    use_item
)

def main():
    # Get player's name
    player_name = input("Enter your name: ")
    print_welcome(player_name)
    player_hp = 30
    player_gold = 100000
    inventory = []
    equipped_weapon = None # Track equipped weapon

    # Main game loop
    while True:
        print("\nYou are in your home village.")
        print(f"Current HP:{player_hp} | Current Gold:{player_gold} | Equipped Weapon:{equipped_weapon['name'] if equipped_weapon else 'None'}")
        print("What would you like to do?")
        print("1. Leave town (Fight Monster)")
        print("2. Sleep (Restore HP for 5 Gold)")
        print("3. Shop")
        print("4. Manage Inventory")
        print("5. Exit Game")
        # Get user choice
        choice = get_user_choice("Enter your choice (1-5): ", ['1', '2', '3', '4', '5'])

        if choice == '1':
            # Fight a monster
            monster = new_random_monster()
            player_hp, player_gold, inventory, equipped_weapon = fight_monster(player_hp, player_gold, monster, inventory, equipped_weapon)
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
            # Define Shop Items
            item1_name = "Sword"
            item1_price = 50.00
            item2_name = "Shield"
            item2_price = 30.00
            item3_name = "Health Potion"
            item3_price = 10.00
            item4_name = "Monster Eliminator"
            item4_price = 25.00
            # Shop menu
            print("Welcome to the shop!")
            print("1. Buy Sword (50 Gold)")
            print("2. Buy Shield (30 Gold)")
            print("3. Buy Health Potion (10 Gold)")
            print("4. Buy Monster Eliminator (25 Gold)")
            print("5. Exit Shop")
            shop_choice = get_user_choice("Enter your choice (1-5): ", ['1', '2', '3', '4', '5'])

            if shop_choice == '1':
                num_purchased, remaining_money = purchase_item(item1_price, player_gold)
                if num_purchased > 0:
                    # Add sword to inventory
                    sword = {
                        'name': 'Sword',
                        'type': 'weapon',
                        'maxDurability': 10,
                        'currentDurability': 10,
                        'note': 'A common sword.'
                    }
                    add_item_to_inventory(inventory, sword)
                    player_gold = remaining_money
                    print(f"Purchased {num_purchased} Sword(s).")
                else:
                    print("Not enough gold to purchase Sword.")
            elif shop_choice == '2':
                num_purchased, remaining_money = purchase_item(item2_price, player_gold)
                if num_purchased > 0:
                    # Add shield to inventory
                    shield = {
                        'name': 'Shield',
                        'type': 'Armor',
                        'note': 'protects the user from attack.'
                    }
                    add_item_to_inventory(inventory, shield)
                    player_gold = remaining_money
                    print(f"Purchased {num_purchased} Shield(s).")
                else:
                    print("Not enough gold to purchase Shield.")
            elif shop_choice == '3':
                num_purchased, remaining_money = purchase_item(item3_price, player_gold)
                if num_purchased > 0:
                    # Add Health Potion to inventory
                    health_potion = {
                        'name': 'Health Potion',
                        'type': 'consumable',
                        'note': 'Restores 10 HP when used.'
                        }
                    add_item_to_inventory(inventory, health_potion)
                    player_gold = remaining_money
                    print(f"Purchased {num_purchased} Health Potion(s)")
                else:
                    print(f"Not enough gold to purchase Health Potions")
            elif shop_choice == '4':
                num_purchased, remaining_money = purchase_item(item4_price, player_gold)
                if num_purchased > 0:
                    # Add Monster Eliminator
                    monster_eliminator = {
                        'name': 'Monster Eliminator',
                        'type': 'consumable',
                        'note': 'Instantly kills any monster'
                        }
                    add_item_to_inventory(inventory, monster_eliminator)
                    player_gold = remaining_money
                    print(f"Purchased {num_purchased} Monster Eliminator(s)")
                else:
                    print("Not enough gold to purchase Monster Eliminator")
                          
        elif choice == '4':
            # Manage Inventory
            print("Inventory items:")
            for idx, item in enumerate(inventory, 1):
                print(f"{idx}. {item['name']} (Type: {item['type']})")
            print("a. Equip Weapon")
            print("b. Use Consumable")
            print("c. Return")
            sub_choice = get_user_choice("Choose an option (a-c): ", ['a','b','c'])
            if sub_choice == 'a':
                equipped_weapon = equip_item(inventory, 'weapon', equipped_weapon)
            elif sub_choice == 'b':
                used = use_item(inventory)
                if used:
                    # If used item is health potion
                    if used['name'] == 'Health Potion':
                        player_hp += 10
                        if player_hp > 30:
                            player_hp = 30
                        print("Health restored by 10.")
                        inventory.remove(used)
                    elif used['name'] == 'Monster Eliminator':
                        # Will be handled during fight
                        print("Monster Eliminator is ready to use in the next fight.")
            else:
                continue
        elif choice == '5':
            print("Thanks for playing!")
            break  # Exit game

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

