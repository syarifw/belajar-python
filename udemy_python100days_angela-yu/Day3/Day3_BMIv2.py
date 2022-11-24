height = float(input("Enter your height in m : \n"))
weight = float(input("Enter your weight in kg : \n"))

bmi_calculator = weight/height**2
print(bmi_calculator)

if (bmi_calculator < 18.5):
    print("You're Under weight")
elif (bmi_calculator <25):
    print("You're Normal weight")
elif (bmi_calculator <30):
    print("You're over weight")
elif (bmi_calculator <35):
    print("You're obese")
else:
    print("You're clinically obese")