#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
eazy_level = []
eazy_level_s = ''

# Syarif Resolve :

# for i in range(0,nr_letters):
#   if nr_letters > 0 :
#     letters_pick = random.randint(0,len(letters)-1)
#     eazy_level.append(letters[letters_pick])

# for j in range(nr_letters,(nr_letters+nr_symbols)):
#   if nr_symbols > 0:
#     symbols_pick = random.randint(0,len(symbols)-1)
#     eazy_level.append(symbols[symbols_pick])

# for k in range((nr_letters+nr_symbols),(nr_letters+nr_symbols+nr_numbers)):
#   if nr_numbers > 0:
#     numbers_pick = random.randint(0,len(numbers)-1)
#     eazy_level.append(numbers[numbers_pick])

# print(''.join(eazy_level))

# Angela Yu Resolve :

# for char in range(1,nr_letters+1):
#     eazy_level_s+=random.choice(letters)
# for sym in range(1,nr_symbols+1):
#     eazy_level_s+=random.choice(symbols)
# for num in range(1,nr_numbers+1):
#     eazy_level_s+=random.choice(numbers)
# print(eazy_level_s)


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

for char in range(1,nr_letters+1):
    eazy_level.append(random.choice(letters))

for char in range(1,nr_symbols+1):
    eazy_level.append(random.choice(symbols))

for char in range(1,nr_numbers+1):
    eazy_level.append(random.choice(numbers))

random.shuffle(eazy_level)

for char in eazy_level:
    eazy_level_s += char

print(eazy_level_s)
