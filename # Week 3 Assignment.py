# Week 3 Assignment.py

# 3 - 1 
names = ['Christopher', 'Lana', 'Jessica', 'Leah', 'Dane', 'Ike' ]
print (names[0])
print (names[1])
print (names [2])
print (names[3])
print (names [4])
print (names[5])

# 3 - 2 - copy and pasted a couple of these to make it quicker
names = ['Christopher', 'Lana', 'Jessica', 'Leah', 'Dane', 'Ike' ]
message = f"Good Morning, hope you have a good day {names[0].title()}"
print (message)
names = ['Christopher', 'Lana', 'Jessica', 'Leah', 'Dane', 'Ike' ]
message = f"Good Morning, hope you have a good day {names[1].title()}"
print (message)
names = ['Christopher', 'Lana', 'Jessica', 'Leah', 'Dane', 'Ike' ]
message = f"Good Morning, hope you have a good day {names[2].title()}"
print (message)
names = ['Christopher', 'Lana', 'Jessica', 'Leah', 'Dane', 'Ike' ]
message = f"Good Morning, hope you have a good day {names[3].title()}"
print (message)
names = ['Christopher', 'Lana', 'Jessica', 'Leah', 'Dane', 'Ike' ]
message = f"Good Morning, hope you have a good day {names[4].title()}"
print(message)
names = ['Christopher', 'Lana', 'Jessica', 'Leah', 'Dane', 'Ike' ]
message = f"Good Morning, hope you have a good day {names[5].title()}"
print(message)

#3-3
Transportation = ['Mototcycle', 'Roller Skates', 'Ford Escape']
message = f"I drive a {Transportation[2].title()}"
print (message)
Transportation = ['Mototcycle', 'Roller Skates', 'Ford Escape']
message = f"I love looking at {Transportation[0].title()}, one day i will own one."
print(message)
Transportation = ['Mototcycle', 'Roller Skates', 'Ford Escape']
message = f"Before I had a car, I would {Transportation[1].title()}"
print(message)

#3 - 4
GuestList = ['Mac Miller', 'Lil Wayne', 'Jack Harlow']
message = f"Would you like to get food {GuestList[0].title()}"
print(message)
GuestList = ['Mac Miller', 'Lil Wayne', 'Jack Harlow']
message = f"What should I make for dinner tonight {GuestList[1].title()}"
print(message)
GuestList = ['Mac Miller', 'Lil Wayne', 'Jack Harlow']
message = f"What is your favorite type of food {GuestList[2].title()}"
print(message)

#3 - 5
GuestList = ['Mac Miller', 'Lil Wayne', 'Jack Harlow']
message = f"Oh no, {GuestList[0]} can't attend dinner tonight."
print (message)
GuestList.append('Kendrick Lamar')
message = f"{GuestList[3].title()} you can join instead if you are free."
print(message)

# 3 - 6 
GuestList.remove('Mac Miller') 
GuestList.insert(0,'Daniel Larson')
GuestList.insert(2,'Lana Del Rey')
GuestList.append("Will Pharell")
print(GuestList)

#3 - 7
message = f"Sorry everyone, I can only bring 2 people to dinner."
print(message)
first_GuestList = GuestList.pop(2)
print(f"{first_GuestList.title()}, sorry you can't come to dinner")
first_GuestList = GuestList.pop(0)
first_GuestList = GuestList.pop(1)
print(GuestList)
first_GuestList = GuestList.pop(0)
print(GuestList)
message = f"Thank you, {GuestList[0]} and {GuestList[1]} for being available to attend dinner."
print(message)

#3 - 8
Locations = ['Peru', 'Bahamas', "Hawaii"]
print (Locations)
print ("\Here is the sorted list:")
print (sorted(Locations))
print (Locations)
print ("\Here are the Locations in reverse order")
Locations.reverse()
print(Locations)
Locations.reverse()
print(Locations)
print (sorted(Locations))
Locations.reverse()
print (sorted(Locations))

#3 - 9
len(GuestList)
print (len(GuestList))

#3 - 10
GuestList = ['Daniel Larson', 'Lil, Wayne', 'Lana Del Rey', 'Jack Harlow', 'Kendrick Lamar','Will Pharell']
first_GuestList = GuestList.pop(0)
first_GuestList = GuestList.pop(1)
GuestList.remove('Jack Harlow')
GuestList.insert(0, 'The Rock')
print(sorted(GuestList))
GuestList.reverse()
