# Syarif Resolution :

import random
from hangman_words import word_list
from hangman_art import stages, logo
from replit import clear

display = []
lives = 6
is_match = True

# Randomized the choosen word
choosen_word = word_list[random.randint(0,len(word_list)-1)]
print(choosen_word)

# Iteration to display the suggestion choosen word
for _ in range(len(choosen_word)):
 display.append("-")

print(logo)
print(''.join(display))

# do guessing until the display has same value with choosen_word
while ''.join(display) != choosen_word and is_match:

  guess = input("Guess a letter : ").lower()
  clear()

  if guess in (''.join(display)):
    print(f"You've already guessed {guess}")
  else :
    for index_letter in range(len(choosen_word)):
      if choosen_word[index_letter] == guess:
        display[index_letter] = guess
    
    if not guess in choosen_word:
      lives-=1
      print(f"You guessed {guess},that's not in the word. You loose a life.")
      if lives <= 0:
        print(stages[lives])
        print("You Loose")
        is_match=False
    elif ''.join(display) == choosen_word:
      is_match=False
      print("You Win")

  print(''.join(display))
  print(stages[lives])
  

# Angela Yu Resolution :

import random
from hangman_art import stages, logo
from hangman_words import word_list
from replit import clear

print(logo)
game_is_finished = False
lives = len(stages) - 1

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

display = []
for _ in range(word_length):
    display += "_"

while not game_is_finished:
    guess = input("Guess a letter: ").lower()

    #Use the clear() function imported from replit to clear the output between guesses.
    clear()

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(f"{' '.join(display)}")

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            game_is_finished = True
            print("You lose.")
    
    if not "_" in display:
        game_is_finished = True
        print("You win.")

    print(stages[lives])