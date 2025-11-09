import random
import os
import time

# Clear screen function
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Snake and Ladder mappings
snakes = {24: 18, 39: 22, 53: 34, 66: 44, 78: 59, 97: 23, 99: 79}  # Snakes - move down if landed on these
ladders = {9: 33, 21: 47, 37: 67, 57: 71, 70: 94, 86: 96}  # Ladders - move up if landed on these

ur_flag = my_flag = 0
ur_game_piece = my_game_piece = 0
game_piece_color_list = ["red", "green", "blue", "yellow"]
bold = '\033[1m'
underline = '\033[4m'
end = '\033[0m'

# Function to set color codes for game piece
def coloring(x):
    colors = {"red": '\033[31m', "green": '\033[32m', "blue": '\033[34m', "yellow": '\033[33m'}
    return colors.get(x)

roll_messages = [
    "Nice! You rolled a 🎲 {}.",
    "Boom! It's a 🎲 {}.",
    "Rolling... and it's a 🎲 {}!",
    "You got a 🎲 {}. Keep going!"
]

# Prompt user to select game piece color
ur_game_piece_color = input(">> Select your game piece color (" + '\033[31m' + "red, " + '\033[32m' + "green, " + '\033[34m' + "blue " + end + "or " + '\033[33m' + "yellow" + end + "): ").lower()
while True:
    if ur_game_piece_color in game_piece_color_list:
        break
    else:
        clear_screen()
        ur_game_piece_color = input(">> Please, choose your game piece color among " + '\033[31m' + "red, " + '\033[32m' + "green, " + '\033[34m' + "blue " + end + "and " + '\033[33m' + "yellow" + end + ": ").lower()
        continue

# Computer selects a game piece color different from the user
print("\nWait, let me select my game piece color...")
time.sleep(1)
my_game_piece_color = random.choice(game_piece_color_list)
while my_game_piece_color == ur_game_piece_color:
    my_game_piece_color = random.choice(game_piece_color_list)
    continue

clear_screen()
game_piece_color = coloring(ur_game_piece_color)
print(f"You select " + game_piece_color + f"{ur_game_piece_color} color" + end, end=" ")
game_piece_color = coloring(my_game_piece_color)
print(f"and I select " + game_piece_color + f"{my_game_piece_color} color" + end, end=". ")
print("Okay! Let's start the game...\n")

# Game loop starts
while True:
    game_piece_color = coloring(ur_game_piece_color)
    while ur_flag == 0:
        input(">> Press enter to rotate the dice 🎲 : ")
        ur_move = random.randint(1, 6)
        if ur_move != 1:
            print(f"You got {ur_move}, but you have to get 1 to start the journey.\n")
            ur_flag = -1
        else:
            clear_screen()
            print("Wow! You got " + game_piece_color + underline + "1" + end + ", you get another chance to rotate the dice.\n")
            ur_game_piece = 1
            ur_flag = 1

    if ur_flag == -1:
        ur_flag = 0

    while ur_flag == 1:
        input(">> Your turn to rotate the dice 🎲 : ")
        ur_move = random.randint(1, 6)
        ur_game_piece += ur_move

        # Check if user lands on a snake or ladder
        if ur_game_piece in snakes:
            clear_screen()
            print(f"Oh no! You landed on a " + underline + bold + "snake" + end + "🐍 at {ur_game_piece}, sliding down to " + game_piece_color + underline + f"{snakes[ur_game_piece]}" + end + "!\n")
            ur_game_piece = snakes[ur_game_piece]
        elif ur_game_piece in ladders:
            clear_screen()
            print(f"Great! You found a " + underline + bold + "ladder" + end + " 🪜 at {ur_game_piece}, climbing up to " + game_piece_color + underline + f"{ladders[ur_game_piece]}" + end + "!\n")
            ur_game_piece = ladders[ur_game_piece]
        
        if ur_game_piece > 100:
            ur_game_piece -= ur_move
            print(f"It's {ur_move}, but you need {100 - ur_game_piece} to win the game.\n")
        else:
            print(random.choice(roll_messages).format(ur_move) + " your piece is now at " + game_piece_color + underline + f"{ur_game_piece}" + end + ".\n")
        break

    game_piece_color = coloring(my_game_piece_color)
    while my_flag == 0:
        print("● It's my turn to roll the dice 🎲 : ")
        time.sleep(0.75)
        my_move = random.randint(1, 6)
        if my_move != 1:
            print(f"I got {my_move}, but I need a 1 to start.\n")
            my_flag = -1
        else:
            clear_screen()
            print(f"Wow! I got 1, I get another chance!\n")
            my_game_piece = 1
            my_flag = 1

    if my_flag == -1:
        my_flag = 0
    
    while my_flag == 1 and ur_game_piece != 100:
        print("● Now it's my turn to roll the dice 🎲 : ")
        time.sleep(0.75)
        my_move = random.randint(1, 6)
        my_game_piece += my_move

        # Check if computer lands on a snake or ladder
        if my_game_piece in snakes:
            clear_screen()
            print(f"Oh no! I landed on a " + underline + bold + "snake" + end + " 🐍 at {my_game_piece}, sliding down to " + game_piece_color + underline + f"{snakes[my_game_piece]}" + end + "!\n")
            my_game_piece = snakes[my_game_piece]
        elif my_game_piece in ladders:
            clear_screen()
            print(f"Yay! I found a " + underline + bold + "ladder" + end + " 🪜 at {my_game_piece}, climbing up to " + game_piece_color + underline + f"{ladders[my_game_piece]}" + end + "!\n")
            my_game_piece = ladders[my_game_piece]
        
        if my_game_piece > 100:
            my_game_piece -= my_move
            print(f"It's {my_move}, but I need {100 - my_game_piece} to win.\n")
        else:
            print(f"It's {my_move}, my piece is now at " + game_piece_color + underline + f"{my_game_piece}" + end + ".\n")
        break
        
    if ur_game_piece == 100:
        print(underline + bold + f"🎉 Congrats! You reached 100. You win! 🏆\n" + end)
        print(input("GAME OVER!!! Press Enter to exit..."))
        break
    elif my_game_piece == 100:
        print(underline + bold + f"🤖 Hooray! I reached 100. I win! 🎊\n" + end)
        print(input("GAME OVER!!! Press Enter to exit..."))
        break
    else:
        continue
