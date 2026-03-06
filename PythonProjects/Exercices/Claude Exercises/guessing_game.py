
import random
secret = random.randint(1,10)
attempts = 1
guess = int(input("Guess the secret number :"))


while guess != secret :
    if guess > secret :
        print("Too high")
    if guess < secret :
        print("Too low")
    attempts = attempts + 1

    guess = int(input("Guess again :"))

print(f"You guessed the secret number after {attempts} attempts")