rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

map = [rock,paper,scissors]

user_pick=int(input("What do you choose ? Type 0 for rock, 1 for paper, 2 for scissors > "))

com_pick = random.randint(0,len(map)-1)

if user_pick >= 3 or user_pick<0:
    print("User pick invalid number")
else:
    print(f"{map[user_pick]}")
    print("Computer choose :")
    print(f"{map[com_pick]}")

if user_pick >=3 or user_pick <0:
  print("You Type invalid number. You Loose.")
elif user_pick == com_pick:
  print("You Draw")
elif user_pick == 0 and com_pick == 2:
  print("You Win")
elif user_pick == 2 and com_pick == 0:
  print("You Loose")
elif user_pick > com_pick:
    print("You Win")
elif user_pick < com_pick:
    print("You Loose")
