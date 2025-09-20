# Assignment 4 

# 4 - 1
pizza = ['margarita', 'ricatta cheese', 'supreme']
for pizza in pizza:
    print (f'My favotire pizza is {pizza.title()}.')
    print (f'I cannot wait to have pizza on friday!')
# 4 - 2
animals = ['Dog', 'Cat', 'Bird']
for animals in animals:
    print (f'A {animals.title()} is a great pet.')
print("These are all great types of pets.")
# 4 - 3
numbers =list(range(1, 21))
print(numbers)
# 4 - 4
numbers =list(range(1, 1000001))
print(numbers)
# 4 - 5
didgits = [1, 100, 500, 1000, 5000, 1000001]
print("Min:", min (numbers))
print("Max:", max(numbers))
total = sum(numbers)
print ("Sum:", total)
# 4 - 6 
for number in range(1, 3, 17):
    print(number)
# 4 - 7
for number in range(3, 9, 15):
    print(number)
# 4 - 8
for number in range(1,11):
    cube = number ** 3
    print(cube)
# 4 - 9
cubes = [number ** 3 for number in range(1,11)]
print(cubes)
# 4 - 10
pizzas = ['margarita', 'delux', 'supreme', 'meat lovers', 'veggie']
print("The first three items in the list are:")
print (pizzas[:3])
middle_index = len(pizzas) //2
print("\nThree items from the middle of the list are:")
print(pizzas[middle_index-1: middle_index+2])
print("\nThe last three items in the list are:")
print(pizzas[-3:])
# 4 - 11
pizzas = ['margarita', 'ricatta cheese', 'supreme']
friend_pizzas = pizzas[:]
pizzas.append ('meat lovers')
friend_pizzas.append('veggie')
print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)
print("My friends favorite pizzas are:")
for pizza in friend_pizzas:
    print(friend_pizzas)
# 4 - 13 
buffet_menu = ['pasta', 'salads', 'pizza', 'mozzarella sticks', 'breads', 'sandwiches']
print('The resturant has all you can eat of:')
for foods in buffet_menu:
    print(foods)
try:
    buffet_menu[3] = 'mozzarella sticks'
except TypeError:
    print("\nYou can get sauce wit it.")
buffet_menu = ('pasta', 'salads', 'pizza', 'mozzarella sticks', 'breads', 'sandwiches')

# 4 - 14
    def buffet_menu():
        print (food)
food = ['pasta', 'salads', 'pizza', 'mozzarella sticks', 'breads', 'sandwich']
