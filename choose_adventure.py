name = input(f"Type your name: ")
print(f"Welcome {name} to this adventure!")

answer = input(
    f"You are on a dirt road, it has come to an end and you can go left or right. Type 'left' or 'right': ")

if answer == "left":
    answer = input(
        f"You come to a river. You can walk around it or swim across. Type 'walk' to walk around or 'swim' to swim across: ")

    if answer == "walk":
        print(f"You swam across and were eaten by an aligator. You lose.")
    elif answer == "swim":
        print(f"You walked for many miles and ran out of water. You lose.")
    else:
        print(f"Not a valid option. You lose.")

elif answer == "right":
    answer = input(
        f"You come to a wobbly bridge. Do you cross or turn back? Type 'cross' to cross or 'back' to turn back: ")

    if answer == "back":
        print(f"You go back and lose.")
    elif answer == "cross":
        answer = input(
            f"You cross the bridge and meet a stranger. Do you talk to them? Type 'yes' or 'no': ")
        if answer == "yes":
            print(f"You talk to the stranger and they give you gold. You WIN!")
        elif answer == "no":
            print(f"You ignore the stranger and they are offended. You LOSE!")
        else:
            print(f"Not a valid option. You lose.")
    else:
        print(f"Not a valid option. You lose.")
else:
    print(f"Not a valid option. You lose.")
