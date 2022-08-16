import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]
options

while True:
    user_input = input(
        f"Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    randome_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    computer_pick = options[randome_number]
    print(f"Computer picked {computer_pick}.")

    if user_input == "rock" and computer_pick == "scissors":
        print(f"You won!")
        user_wins += 1
    elif user_input == "paper" and computer_pick == "rock":
        print(f"You won!")
        user_wins += 1
    elif user_input == "scissors" and computer_pick == "paper":
        print(f"You won!")
        user_wins += 1
    else:
        print(f"You lost!")
        computer_wins += 1

print(f"You won {user_wins} times!")
print(f"The computer won {computer_wins} times!")
print(f"Goodbye!")
