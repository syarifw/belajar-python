#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random

print("Welcome to the number guessing Game!\nI'm thinking of number between 1 and 100")

guessing_number = random.choice(range(1,101))
print(guessing_number)

difficulity = input("Choose difficulity. type 'easy' or 'hard' : ")

if difficulity == 'easy':
  attempt_balance = 10
else:
  attempt_balance = 5
print(attempt_balance)

while attempt_balance > 0:
  print(f"You have {attempt_balance} remaining to guess the number.")
  guess_number = int(input("Make a guess : "))
  if guess_number == guessing_number:
    attempt_balance = 0
    print(f"You got it ! the answer is {guess_number}")
  elif guess_number < guessing_number:
    attempt_balance -= 1
    print("Too low")
  elif guess_number > guessing_number:
    attempt_balance -=1
    print("Too high")
  
  if attempt_balance == 0:
    print("You've run out guess out. You lose.")
  else:
    print("Guess Again.")

