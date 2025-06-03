import random


secret_number = random.randint(1, 100)
attempts = 0
guessed_correctly = False

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

while not guessed_correctly:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            guessed_correctly = True
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
    except ValueError:
        print("Please enter a valid integer.")
