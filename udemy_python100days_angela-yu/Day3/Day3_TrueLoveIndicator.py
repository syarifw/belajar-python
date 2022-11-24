# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

combined_name = name1+name2
combined_name_lower = combined_name.lower()

count_t = combined_name_lower.count('t')
count_r = combined_name_lower.count('r')
count_u = combined_name_lower.count('u')
count_e = combined_name_lower.count('e')
count_l = combined_name_lower.count('l')
count_o = combined_name_lower.count('o')
count_v = combined_name_lower.count('v')
count_e2 = combined_name_lower.count('e')

total_true = int(count_t) + int(count_r) + int(count_u) + int(count_e)

total_love = int(count_l) + int(count_o) + int(count_v) + int(count_e2)

total_true_love = int(str(total_true)+str(total_love))

if (total_true_love < 10 or total_true_love > 90):
  print(f"Your score is {total_true_love}, you go together like coke and mentos.")
elif (total_true_love <50 and total_true_love >40):
  print(f"Your score is {total_true_love}, you are alright together.")
else:
  print(f"Your score is {total_true_love}")

#Write your code below this line 👇


