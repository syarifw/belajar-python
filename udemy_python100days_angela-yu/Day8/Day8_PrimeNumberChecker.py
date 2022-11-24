# Syarif Resolution

#Write your code below this line 👇

def prime_checker(number):
  counter_prime_checker = 0
  for i in range(1,11):
    if number % i == 0 and number % number == 0:
      counter_prime_checker+=1

  if counter_prime_checker < 2:
    print("It's prime number")
  else:
    print("It's not prime number")
    
#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)


# Angela Yu Resolution

