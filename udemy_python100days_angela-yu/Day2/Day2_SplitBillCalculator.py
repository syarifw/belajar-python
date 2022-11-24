
print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill ? $"))
persentage_tip = int(input("What percentage tip would you like to give ? 10, 12, or 15 ?"))
total_people = int(input("How many people to split the bill? "))

bill_per_person = round((total_bill+(total_bill*persentage_tip/100))/total_people,2)

print(f"Each Person should pay: ${bill_per_person:.2f}")