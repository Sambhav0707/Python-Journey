import random

def game():
    # 1. Generate a new number
    new_num = random.randint(1, 69)
    print(f"Generated number: {new_num}")

    old_num = None # A placeholder for the old score

    # 2. Try to READ the existing score
    try:
        # Open in 'r' (read) mode
        with open("game.txt", "r") as f:
            # Read, remove whitespace, and convert to an integer
            old_num = int(f.read().strip())
            print(f"Current score in file: {old_num}")
            
    except (FileNotFoundError, ValueError):
        # This catches two errors:
        # 1. FileNotFoundError: It's the first time running the game.
        # 2. ValueError: The file was empty or had bad text.
        print("No valid score found in file.")
        
    # 3. Compare and decide whether to WRITE
    # Write if (A) there was no old number OR (B) the new number is lower
    if old_num is None or new_num < old_num:
        print(f"New low score! Saving {new_num}.")
        # Open in 'w' (write) mode to erase and save the new low score
        with open("game.txt", "w") as f:
            f.write(str(new_num)) # Must write a string
    else:
        print(f"{new_num} is not lower than {old_num}. No change.")

# Run the game
game()