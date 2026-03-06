
import random
secret = random.randint(1,10)
attempts = 1

def get_guess(prompt):
    while True:
        try:
            guess = int(input(prompt))
            if guess < 1 or guess > 10:
                print("Out of range! Please enter a number between 1 and 10.")
            else:
                return guess
        except ValueError:
            print("Invalid input! Please enter a number.")

guess = get_guess("Guess the secret number :")


while guess != secret :
    if guess > secret :
        print("Too high")
    if guess < secret :
        print("Too low")
    attempts = attempts + 1

    guess = get_guess("Guess again :")

print(f"You guessed the secret number after {attempts} attempts")