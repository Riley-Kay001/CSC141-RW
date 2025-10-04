#6 - 1 - Person
person_1 = {'first_name': 'Chris', 'last_name' : 'Connors', 'age' : 20, 'city' : 'Denton, MD'}

print(person_1['first_name'])
print(person_1['last_name'])
print(person_1['age'])
print(person_1['city'])

#6 - 2 - Favorite Numbers
favorite_numbers = {'Chris' : 7 , 'Riley' : 18 , 'Leah' : 50 , 'Dane' : 26}

person_1 = favorite_numbers['Chris']
print(f"Chris's favorite number is {person_1}")

person_2 = favorite_numbers['Riley']
print(f"Riley's favorite number is {person_2}")

person_3 = favorite_numbers['Leah']
print(f"Leahs's favorite number is {person_3}")

person_4 = favorite_numbers['Dane']
print(f"Dane's favorite number is {person_4}")

#6 - 3 - Glossary
glossary = {'variable' : 'stores data values','loop' : 'A sequence that is continually repeated until a certain condition is met' ,'list' : 'A collection of items in order'}
for word, meaning in glossary.items():
    print(f"{word}:\n {meaning}\n")
          
#6 - 4 - Glossary clean up 
glossary = {'variable' : 'store data values.', 'loop' : 'A sequence that is continually repeated until a certain condition is met', 'list' : 'A collection of items in order', 'if statement' : 'A conditional statement used to make decisions in code.', 'dictionary' : 'A collection of words'}
for word, meaning in glossary.items():
    print(f"{word}:\n {meaning}\n")

#6 - 5 - Rivers
rivers = {'Colorado River' : 'From Rocky Mountains to Gulf of California' , 'Mississippi River' : 'Mississipi - Missouri' , 'Ohio River' : 'Ohio'}
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")
    print("\nRivers included in the dictionary:")
for river in rivers.keys():
    print(f"- {river.title()}")
    print("\nFound in the dictionary:")
for place in rivers.values():
    print(f"- {place.title()}")

#6 - 6 - Polling 
favorite_languages_poll = {'Chris' : 'Python', 'Ike' : 'Java', 'Dane' : 'C++'}
people_to_poll = ['Chris', 'Ike', 'Dane']
for person in people_to_poll:
    print(f"Thank you for taking the poll, {person.title()}.")
else:
    print(f"{person.title()}, pleace take our poll to see your favorite programming language.")

#6 - 7 - People
person_dictionary1= {'first_name' : 'Riley', 'last_name' : 'Winchell', 'age' : 19, 'city' : 'Castle Rock, CO'}
person_dictionary2 = {'first_name': 'Jessica', 'last_name' : 'Winchell', 'age' : 42, 'city' : 'Lancaster, CA'}
person_1 = {'first_name': 'Chris', 'last_name' : 'Connors', 'age' : 20, 'city' : 'Denton, MD'}
people = [person_dictionary1, person_dictionary2, person_1]
for person in people:
    print("\nPerson Info:")
    for key, value in person.items():
        print(f"{key.replace('_', ' ').title()}: {value}")

#6 - 8 - Pets
animal_1 = {'Animal' : 'dog' , 'owner' : 'Riley'}

animal_2 = {'Animal' : 'cat' , 'owner' : 'Chris'}

animal_3 = {'Animal' : 'chicken' , 'owner' : 'Leah'}

animals = [animal_1, animal_2, animal_3]
for animal in animals:
    print("\nPet Info:")
for key, value in animal.items():
    print(f"{key.title()}: {value}")

#6 - 9 -
favorite_places = {'Chris' : ['beach' , 'buffet', 'Maryland'] , 'Dane' : ['mall', 'amuesment park'], 'Jessica' : ['Colorado', 'lake']}
for person, places in favorite_places.items():
    print(f"\n{person}'s favorite places are:")
    for place in places:
        print(f"- {place}")
