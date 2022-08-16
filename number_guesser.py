import random

top_of_range = input(f"Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print(f"Please type a number larger than 0 next time.")
        quit()
else:
    print(f"Please type a number next time.")
    quit()

random_number = random.randint(0, top_of_range)

guesses = 0

while True:
    guesses += 1
    user_guess = input(f"Make a guess: ")

    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print(f"Please type a number next time.")
        continue

    if user_guess == random_number:
        print(f"You got it!")
        break
    elif user_guess > random_number:
        print(f"You were above the number.")
        continue
    elif user_guess < random_number:
        print(f"You were below the number.")
        continue

print(f"You got it in {guesses} guesses!")
