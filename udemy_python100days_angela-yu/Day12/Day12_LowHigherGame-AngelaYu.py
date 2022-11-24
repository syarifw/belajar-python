import random

EASY_LEVEL = 10
HARD_LEVEL = 5
attempt_balance = 0

def level_game():
    level = input("Choose difficulity. Type 'easy' or 'hard' : ")
    if level == 'easy':
        return EASY_LEVEL
    elif level == 'hard':
        return HARD_LEVEL
    else:
        return 0

def compare(guess_number,random_number,attempt_balance):
    if guess_number == random_number:
        print(f"You got it ! The answer was {guess_number}")
        return
    elif guess_number < random_number:
        print("Too Low.")
        return attempt_balance -1
    elif guess_number > random_number:
        print("Too High")
        return attempt_balance -1

def game():
    print("Welcome to the Guessing Number Game!")
    print("I'm thinking of a number between 1 and 100")

    random_number = random.choice(range(1,101))
    print(f"random number {random_number}")

    attempt_balance = level_game()

    guess_number = 0
    while guess_number != random_number:
        print(f"attempt balance : {attempt_balance}")
        guess_number = int(input("Make a guess : "))
        attempt_balance = compare(guess_number,random_number,attempt_balance)

        if attempt_balance >=1 and guess_number != random_number:
            print("Guess again")
        elif attempt_balance < 1 and guess_number != random_number:
            print("You've run out guess, you lose.")
            return
        else:
            guess_number = random_number

game()



