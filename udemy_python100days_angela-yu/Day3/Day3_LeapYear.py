year_input = int(input("Input a year >\n"))

if (year_input % 4 == 0):
    if (year_input % 100 == 0):
        if (year_input % 400 == 0):
            print("Leap Year")
        else :
            print("Not Leap Year")
    else:
        print("Leap Year")
else:
    print("Not Leap Year")