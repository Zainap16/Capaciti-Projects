import random


def generate_random_number():
    return random.randint(1, 20)


random_number = generate_random_number()

while True:
    guess = int(input("Guess the number (between 1 and 20): "))

    if guess < random_number:
        print("Too low!")
    elif guess > random_number:
        print("Too high!")
    else:
        print("Congratulations! You guessed the number correctly!")
        break
