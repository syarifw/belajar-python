import random

random_int = random.randint(1,9)

# How To Create a random decimal number between 0-5 (five not included) ?

random_float = random.random() * 5
print(f"{random_float:.2f}")


# How to create Heads or Tails on CLI

radom_int = random.randint(0,1)

if radom_int == 0:
  print("Heads")
else:
  print("Tails")
