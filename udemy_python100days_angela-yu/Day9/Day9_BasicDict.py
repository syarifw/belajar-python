programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.", 
  "Function": "A piece of code that you can easily call over and over again.",
  "Loop": "The action of doing something over and over again"
}

# -- Add new element on programming_dictionary
# programming_dictionary["Assigment"] = "Give something a new value"

# -- Create new dictionary 
juice = {}

# -- Wipe old dictionary 
# programming_dictionary = {}

# -- Edit value on dictionary
# programming_dictionary['Bug'] = "samething with insect"

# -- How to access the dictionary
for key in programming_dictionary:
  print(programming_dictionary[key]) # for in will access the key of dictionary only


# Dict in Dict

travel_log = {
  "France": [
      {
        "visited_city":["Paris","Lille","Dijon"],
        "total_visited":12
      }
    ],
  "Germany" : [
      {
        "visited_city":["Berlin","Hamburg","Stuttgart"],
        "total_visited":15
      }
    ]
}

# Dict in List

travel_log1 = [
  {
    "country":"France",
    "visited_city": ["Paris","Lille","Dijon"],
    "total_visited":12
  },
  {
    "country":"Germany",
    "visited_city": ["Berlin","Hamburg","Stuttgart"],
    "total_visited":15
  }
]