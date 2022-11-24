# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

# Multiple input, positional parameter
def greet(stat1,stat2,stat3):
  print(f"{stat1},{stat2},{stat3}")

greet("Halo","Kamsihamida","Bonjour")

# Multiple input,  keyword parameter
def kudos(name,location):
  print(f"Hello {name}, thank you for coming to {location}")

kudos(location="Bandung",name="Syarif")

# Note :
# - stat1 is a parameter, "Halo" is argument
