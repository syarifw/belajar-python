import random
from art import logo
from replit import clear

def pick_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_card(cards):
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  if 11 in cards and sum(cards) > 21:
    index_ace = cards.index(11)
    cards[index_ace] = 1
  return sum(cards)

def compare (user_score,com_score):
  if user_score > 21 and com_score > 21:
    return "You loose1"

  if user_score == com_score:
    return "Draw1"
  elif user_score == 0:
    return "You win1"
  elif com_score == 0:
    return "Com win1"
  elif user_score > 21:
    return "You loose2"
  elif com_score > 21:
    return "You Win2"
  elif user_score > com_score:
    return "You Win3"
  else:
    return "You Loose3"
  
def black_jack():

  print(logo)

  user_cards = []
  com_cards = []
  is_game_over = False

  for _ in range(2):
    user_cards.append(pick_card())
    com_cards.append(pick_card())

  while not is_game_over:
    user_score = calculate_card(user_cards)
    com_score = calculate_card(com_cards)

    print(f"User cards = {user_cards}")
    print(f"Com cards = {com_cards} ")

    # print(compare(user_score,com_score))

    if user_score == 0 or com_score == 0 or user_score > 21:
      is_game_over = True
      print("Masuk Sini")
    else :
      need_draw_again = input("Need to draw again ? type 'y' or 'n' > ")
      if need_draw_again == "y":
        user_cards.append(pick_card())
      else:
        print("Masuk Situ")
        is_game_over = True

  while com_score != 0 and com_score < 17:
    print("Masuk Sono")
    com_cards.append(pick_card())
    com_score = calculate_card(com_cards)

  print(f"Your latest cards : {user_cards}, total : {user_score}")
  print(f"Com latest cards : {com_cards}, total : {com_score}")
  print(compare(user_score,com_score))

while input("Need to play blackjack ? 'y' or 'n'") == "y":
  clear()
  black_jack()