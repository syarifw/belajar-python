# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
# print(student_heights)
indeks = 0
sum_of_heights = 0

for check_average in student_heights:
  indeks += 1
  sum_of_heights += check_average

average_heights = sum_of_heights/indeks
print(round(average_heights))


# for loop to check max height on student_height
max_height=0

for check_max in student_heights:
  if check_max > max_height:
    max_height = check_max