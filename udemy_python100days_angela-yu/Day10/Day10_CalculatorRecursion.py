# Syarif Resolution

# *** USE RECURSION ***

# NOT3 : Be Carefull to use Recursion trick. Harus cermat memainkan flag dan kondisi yang ada sebelumnya
#        agar terhindar dari infinite loop

from art import logo
from replit import clear

is_still_continue = True


while is_still_continue:
  answer = ''
  is_cont = ''
  clear()
  print(logo)
  def add(n1,n2):
    return n1+n2
  def substract(n1,n2):
    return n1-n2
  def multiply(n1,n2):
    return n1*n2
  def divide(n1,n2):
    return n1/n2

  calculator_opr_dict = {
    "+":add,
    "-":substract,
    "x":multiply,
    ":":divide
  }

  num_first = int(input("Type for first number > "))
  for operator in calculator_opr_dict:
    print(operator)
  
  should_continue = True
  while should_continue:
    operator = input("Choose the operator > ")
    num_next = int(input("Type the next number > "))

    answer = calculator_opr_dict[operator](num_first,num_next)
    print(f"{int(answer)}")
  
    is_cont = input(f"Type 'y' to continue calculate with {answer}, and 'n' with exit.")

    if is_cont == "y":
      num_first = answer
    elif is_cont == "n":
      should_continue = False


# Angela Yu Resolution

from art import logo
from replit import clear

# is_still_continue = True

def calculator():
  answer = ''
  is_cont = ''
  clear()
  print(logo)
  def add(n1,n2):
    return n1+n2
  def substract(n1,n2):
    return n1-n2
  def multiply(n1,n2):
    return n1*n2
  def divide(n1,n2):
    return n1/n2

  calculator_opr_dict = {
    "+":add,
    "-":substract,
    "x":multiply,
    ":":divide
  }

  num_first = float(input("Type for first number > "))
  for operator in calculator_opr_dict:
    print(operator)
  
  should_continue = True
  while should_continue:
    operator = input("Choose the operator > ")
    num_next = float(input("Type the next number > "))

    answer = calculator_opr_dict[operator](num_first,num_next)
    print(f"{float(answer)}")
  
    is_cont = input(f"Type 'y' to continue calculate with {answer}, and 'n' with exit.")

    if is_cont == "y":
      num_first = answer
    elif is_cont == "n":
      should_continue = False
      calculator()

calculator()


