import random

playing = True
number = random.randint(5,10)

print("I will genrate n.o from 50 to 100 you need to gess it")

while playing:
    guess = int(input("enter your gess"))

    if guess > number:
        print("your guess is to high")

    elif guess < number:
        print("you guess is too low")

    elif guess == number:
        print("you are right")
        playing = False
        break
