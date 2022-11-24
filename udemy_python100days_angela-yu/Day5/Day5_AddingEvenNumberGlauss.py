#Write your code below this row 👇
buffer_number = 0
for number in range(2,101,2):
  buffer_number += number

print(buffer_number)

for number2 in range(1,101):
  if number2 % 2 == 0:
    buffer_number += number2
print(buffer_number)