travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

def add_new_country(country,sum_visit,sum_city_visit):
  # mapping the paramater on a object
  add_object = {
    "country":country,
    "visits":sum_visit,
    "cities":sum_city_visit
  }
  travel_log.append(add_object)




#🚨 Do not change the code below
add_new_country(country="Russia",sum_visit=2, sum_city_visit=["Moscow", "Saint Petersburg"])
print(travel_log)
