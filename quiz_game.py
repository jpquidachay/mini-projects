print(f"Welcome to my computer quiz!")

playing = input(f"Do you want to play? ")

if playing.lower() != "yes":
    quit()

print(f"Okay! Let's play :)")

score = 0

answer = input(f"What does CPU stand for? ")
if answer.lower() == "central processing unit":
    score += 1
    print(f"Correct!")
else:
    print(f"Incorrect!")

answer = input(f"What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    score += 1
    print(f"Correct!")
else:
    print(f"Incorrect!")

answer = input(f"What does RAM stand for? ")
if answer.lower() == "random access memory":
    score += 1
    print(f"Correct!")
else:
    print(f"Incorrect!")

answer = input(f"What does PSU stand for? ")
if answer.lower() == "power supply":
    score += 1
    print(f"Correct!")
else:
    print(f"Incorrect!")

print(f"You got {score} questions correct!")
print(f"You got " + str((score / 4) * 100) + "%")
