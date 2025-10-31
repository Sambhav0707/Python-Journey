import random

'''
Snake: 1
Water: 0
Gun:  -1
'''

# 1. Let the computer make a random choice from the possible values
computer = random.choice([1, 0, -1])

# 2. Get the user's input
userInput = input("Enter your choice ('s' for Snake, 'w' for Water, 'g' for Gun): ")

gameDict = {
    "s": 1,
    "w": 0,
    "g": -1
}

# 3. Check for invalid input
if userInput not in gameDict:
    print("Invalid input! Please enter 's', 'w', or 'g'.")
else:
    user = gameDict[userInput]

    # 4. Print choices
    # (We need to find the key for the computer's choice to print it)
    reverseGameDict = {1: "Snake", 0: "Water", -1: "Gun"}
    print(f"You chose:     {reverseGameDict[user]}")
    print(f"Computer chose: {reverseGameDict[computer]}")

    # 5. Determine the winner
    
    # --- Case 1: Draw ---
    if user == computer:
        print("It's a DRAW!")
        
    # --- Case 2: User Wins ---
    # Snake (1) beats Water (0)
    # Water (0) beats Gun (-1)
    # Gun (-1) beats Snake (1)
    elif (user == 1 and computer == 0) or \
         (user == 0 and computer == -1) or \
         (user == -1 and computer == 1):
        print("🎉 You WIN! 🎉")

    # --- Case 3: Computer Wins (all other possibilities) ---
    else:
        print("💻 Computer Wins! 💻")