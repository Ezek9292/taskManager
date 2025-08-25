import time

def get_player_info():
    """
    Prompts the user for their name and starting budget.
    Returns the name and budget.
    """
    print("Welcome to the Adventure Game!")
    player_name = input("What is your name? ")
    
    # Use a loop to ensure the user enters a valid number for the budget
    while True:
        try:
            budget = float(input(f"Hello, {player_name}. What is your starting budget? "))
            if budget <= 0:
                print("Your budget must be a positive number. Please try again.")
            else:
                print(f"\nExcellent! You begin your journey with ${budget:.2f}.\n")
                return player_name, budget
        except ValueError:
            print("That's not a valid number. Please enter a numerical value for your budget.")

def decision_point_1(budget, inventory):
    """
    First decision point: a marketplace where the player can buy items.
    Uses a loop and conditionals.
    """
    print("--- You arrive at a bustling marketplace. ---")
    time.sleep(1)
    print("A merchant approaches you with two items for sale:")
    print("1. A sturdy leather backpack ($50)")
    print("2. A magical health potion ($20)")
    
    while True:
        choice = input("Enter '1' to buy the backpack, '2' to buy the potion, or '3' to leave the marketplace: ")
        
        if choice == '1':
            if budget >= 50:
                budget -= 50
                inventory.append("Leather Backpack")
                print("You've purchased the backpack. It's a wise investment!")
                print(f"Remaining budget: ${budget:.2f}\n")
            else:
                print("You don't have enough money for the backpack.")
        elif choice == '2':
            if budget >= 20:
                budget -= 20
                inventory.append("Health Potion")
                print("You've purchased the health potion. It shimmers in your hand.")
                print(f"Remaining budget: ${budget:.2f}\n")
            else:
                print("You can't afford that potion right now.")
        elif choice == '3':
            print("You decide to save your money and continue on your journey.\n")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
            
    return budget, inventory

def decision_point_2(budget, inventory):
    """
    Second decision point: choosing a path.
    Uses conditionals.
    """
    print("--- Your path splits into two directions. ---")
    time.sleep(1)
    print("The left path leads through a dark forest, and the right path winds along a sunny river.")
    
    choice = input("Which path do you take? (forest/river): ").lower()
    
    if choice == 'forest':
        print("The forest is eerie, but you find a hidden chest containing a bag of gold!")
        budget += 100
        inventory.append("Bag of Gold")
        print(f"Your budget has increased! New budget: ${budget:.2f}\n")
    elif choice == 'river':
        print("The river path is peaceful. You find a rare, exotic flower growing on the bank.")
        inventory.append("Exotic Flower")
        print("The flower is a beautiful keepsake for your collection.\n")
    else:
        print("You hesitate and end up taking a different, uneventful path. Nothing happens.\n")
        
    return budget, inventory

def decision_point_3(budget, inventory):
    """
    Third decision point: a riddle challenge.
    Checks for a specific item in the inventory to offer a bonus.
    """
    print("--- A mysterious troll blocks your way. ---")
    time.sleep(1)
    print("The troll says, 'Answer my riddle and I will let you pass.'")
    
    if "Bag of Gold" in inventory:
        print("Troll: 'I am rich in minerals but cannot eat. What am I?'")
        print("You realize the riddle is simple if you have a Bag of Gold.")
        answer = "a mine" # The correct answer, but we'll handle any input
        
        # This is a bonus for having the item
        print("You confidently answer 'A mine!'")
        print("The troll is impressed and gives you a magical artifact!")
        inventory.append("Magical Artifact")
        print("You gain a powerful new item.\n")
    else:
        print("Troll: 'What has an eye but cannot see?'")
        answer = input("What is your answer? ").lower()
        if answer == 'a needle':
            print("The troll grunts, 'Correct! You may pass.'")
        else:
            print("The troll growls, 'Incorrect! You must pay the toll!'")
            if budget >= 30:
                budget -= 30
                print(f"You reluctantly pay $30. Remaining budget: ${budget:.2f}\n")
            else:
                print("You don't have enough money and must give up an item.")
                if len(inventory) > 0:
                    lost_item = inventory.pop(0)
                    print(f"The troll takes your {lost_item} instead. You feel its loss.\n")
                else:
                    print("You have no items to give and are forced to turn back.\n")
                    # No new item added

    return budget, inventory

def decision_point_4(budget, inventory):
    """
    Final decision point: an opportunity to invest your remaining budget.
    """
    print("--- You reach the end of your journey. ---")
    time.sleep(1)
    print("A wise old merchant offers you a final chance to increase your fortune.")
    print("He offers to double your money if you invest at least $100.")
    
    choice = input("Do you want to invest? (yes/no): ").lower()
    
    if choice == 'yes':
        if budget >= 100:
            print("You bravely invest $100. The merchant doubles your money!")
            budget += 100  # Invests $100, gets $200 back, so a net gain of $100
        else:
            print("You don't have enough to invest and miss the opportunity.")
    elif choice == 'no':
        print("You decide to play it safe and hold onto your money.")
    else:
        print("Unsure, you miss the opportunity to invest.")

    return budget, inventory

def end_game(player_name, initial_budget, final_budget, inventory):
    """
    Prints the final summary of the game, including stats and a win/loss message.
    """
    print("\n--- The Adventure Comes to an End ---")
    print(f"Final Report for {player_name}:")
    print(f"Initial Budget: ${initial_budget:.2f}")
    print(f"Final Budget:   ${final_budget:.2f}")
    
    print("\nItems Collected:")
    if inventory:
        for item in inventory:
            print(f"- {item}")
    else:
        print("None.")
        
    print("\n--- Game Result ---")
    if final_budget > initial_budget:
        print(f"Congratulations, {player_name}! You've successfully navigated the challenges and ended with a greater fortune. You WIN!")
    elif final_budget == initial_budget:
        print(f"You finished with the same budget you started with. A cautious but successful journey!")
    else:
        print(f"Unfortunately, your final budget is less than your starting budget. You had a tough journey, but lived to tell the tale.")

def main():
    """
    Main function to run the game flow.
    """
    player_name, budget = get_player_info()
    initial_budget = budget
    inventory = []

    # Game decision points
    budget, inventory = decision_point_1(budget, inventory)
    budget, inventory = decision_point_2(budget, inventory)
    budget, inventory = decision_point_3(budget, inventory)
    budget, inventory = decision_point_4(budget, inventory)

    end_game(player_name, initial_budget, budget, inventory)

if __name__ == "__main__":
    main()
