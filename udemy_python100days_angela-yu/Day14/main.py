#import random module and clear on replit
import random
from replit import clear

#import art, game_data
from art import logo,vs
from game_data import data


def main_game():
  print(logo)
  state_main_game = True
  length_data = len(data)-1
  sum_right_answer = 0
  first_index = random.randint(0,length_data)
  second_index = random.randint(0,length_data)

  while state_main_game:
    first_index = second_index
    second_index = random.randint(0,length_data)

    if first_index == second_index:
      second_index = random.randint(0,length_data)

    print(f"Compare A : {data[first_index]['name']}, a {data[first_index]['description']} from {data[first_index]['country']}")
    print(vs)
    print(f"Against B : {data[second_index]['name']}, a {data[second_index]['description']}, from {data[second_index]['country']}")
    
    answer = input("Who has more followers ? Type 'A' or 'B' : ").upper()
    
    if answer == 'A':
      if data[first_index]['follower_count'] > data[second_index]['follower_count']:
        sum_right_answer += 1
        clear()
        print(logo)
        print(f"You're Right A, score= {sum_right_answer}")
      else:
        print(f"You Wrong A, followers {data[first_index]['name']} = {data[first_index]['follower_count']}, while followers {data[second_index]['name']} = {data[second_index]['follower_count']}. Score : {sum_right_answer}")
        state_main_game = False
    elif answer == 'B':
      if data[first_index]['follower_count'] < data[second_index]['follower_count']:
        sum_right_answer += 1
        clear()
        print(logo)
        print(f"You're Right B, score= {sum_right_answer}")
      else:
        print(f"You Wrong B, followers {data[first_index]['name']} = {data[first_index]['follower_count']}, while followers {data[second_index]['name']} = {data[second_index]['follower_count']}. Score : {sum_right_answer}")
        state_main_game = False

    
main_game()