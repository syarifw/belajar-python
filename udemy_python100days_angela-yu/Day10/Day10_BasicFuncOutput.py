# *** FUNCTION WITH OUTPUT ***

def format_name(f_name,l_name):
  if f_name == "" or l_name == "":
    return "You typed an empty string"
  full_name = (f_name+" "+l_name).title()
  return full_name

fullname = input("Insert your firstname : ")
lastname = input("Insert your lastname : ")

output = format_name(f_name=fullname,l_name=lastname)
print(output)
