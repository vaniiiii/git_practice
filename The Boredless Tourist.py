destinations =["Paris, France", "Shanghai, China", "Los Angeles, USA", "Sao Paulo, Brazil", "Cairo, Egypt"]
test_traveler = ['Erin Wilkes', "Shanghai, China", ['historical site', 'art']]

def get_destination_index(destination):
  for i in range(len(destinations)):
    if destination == destinations[i]:
      return i
      break
    else:
      continue

"""
print(get_destination_index("Los Angeles, USA"))
print(get_destination_index("Paris, France"))
print(get_destination_index("Mumbai,India"))
""" 

def get_traveler_location(traveler):
  return get_destination_index(traveler[1])

test_destination_index = get_traveler_location(test_traveler)
# print(test_destination_index)
attractions = [[] for destination in destinations]
# print(attractions)

def add_attraction(destination, attraction):
  try: 
    destination_index = get_destination_index(destination)
    attractions_for_destination = attractions[destination_index]
    attractions_for_destination.append(attraction)
    return attractions_for_destination
  except ValueError:
    return 
  
add_attraction("Los Angeles, USA", ['Venice Beach', ['beach']])


add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("Sao Paulo, Brazil", ["Sao Paulo Zoo", ["zoo"]])
add_attraction("Sao Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])
#print(attractions)

def find_attractions(destination,interests):
  destination_index = get_destination_index(destination)
  attractions_in_city = attractions[destination_index]
  attractions_with_interest =[]
  for attraction in attractions_in_city:
    possible_attraction = attraction
    attraction_tags = possible_attraction[1]
    for interest in interests:
      for tag in attraction_tags:
       if interest == tag:
        attractions_with_interest.append( possible_attraction[0])
       else:
        continue
  return attractions_with_interest
la_arts = find_attractions("Los Angeles, USA", ['art'])
#print(la_arts)


def get_attractions_for_traveler(traveler):
  traveler_destination = traveler[1]
  traveler_interest = traveler[2]
  traveler_attractions = find_attractions(traveler_destination, traveler_interest)
  interests_string = "Hi "
  interests_string= interests_string + traveler[0]
  interests_string = interests_string + ", we think you'll like these places around " + traveler_destination + " :"
  for attraction in traveler_attractions:
    interests_string = interests_string + " " + attraction 
  return interests_string

smills_france = get_attractions_for_traveler(['Dereck Smill', 'Paris, France', ['monument']])
print(smills_france)

