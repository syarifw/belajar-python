alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
 'k', 'l', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
from art import logo

print(logo)
is_finished = False

def caisar(direction,early_text,shift):
  changed_text = ''
  if direction == "decode":
    shift *= -1
  for char in early_text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift
      changed_text += alphabet[new_position]
    else:
      changed_text += char
  print(f"Her's the {direction} result = {changed_text}")


while not is_finished:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number :\n"))

  shift = shift % 26

  caisar(direction=direction, early_text=text, shift=shift)

  is_continue = input("Type 'yes' if you want to go again. Otherwise, type 'no':\n")
  if is_continue == 'no':
    is_finished = True
    print("Sampai Jumpa")

# #TODo-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 

# def caesar(start_text, shift_amount, cipher_direction):
#   end_text = ""
#   if cipher_direction == "decode":
#       shift_amount *= -1
#   for letter in start_text:
#     position = alphabet.index(letter)
#     new_position = position + shift_amount
#     end_text += alphabet[new_position]
#   print(f"Here's the {direction}d result: {end_text}")


# #TOpO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
# caesar(start_text=text, shift_amount=shift, cipher_direction=direction)