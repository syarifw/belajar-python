print("Welcome to Python Pizza Deliveries")
size_of_pizza = input("What size Pizza do you want ? Small/Medium/Large >")
is_add_pepperoni = input("Do you want to add pepperoni ? y/n >")
is_add_cheese = input("Do you want to extra cheese ? y/n >")

bill_of_pizza = 0

if size_of_pizza == "Small":
    bill_of_pizza += 15
elif size_of_pizza == "Medium":
    bill_of_pizza += 20
elif size_of_pizza == "Large":
    bill_of_pizza += 25
else :
    print("You haven't pick the right size yet")

if is_add_pepperoni == "y" :
    if size_of_pizza == "Small":
        bill_of_pizza += 2
    else :
        bill_of_pizza += 3 

if is_add_cheese == "y" :
    bill_of_pizza += 1

print(f"Your total bill : $ {bill_of_pizza}")