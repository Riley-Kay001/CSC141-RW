# 5 - 1
car = 'ford escape'
car == 'bmw'
car == 'ford escape'
age = 19
print == 10
print == 19
Temperature = 90
Temperature < 100
Temperature <= 90
fast_food = ['Chick-Fil-A', 'McDonalds', 'Wendys']
'Chick-Fil-A' in fast_food
'Panda Express' in fast_food
#5.2
fruit = 'Apple'
print("Is fruit == 'Apple'? I predict True.")
print(fruit == 'Apple')
print("\nIs fruit != 'Apple'? I predict False.")
print(fruit != 'Apple')
print("\nIs fruit.lower() == 'apple'? I predict True.")
print(fruit.lower() == 'apple')
print("\nIs fruit.lower() == 'cherries'? I predict False.")
print(fruit.lower() == 'cherries')
num = 10
print("\nIs num == 10? I predict True.")
print(num == 10)
print("\nIs num != 10? I predict False.")
print(num != 10)
print("\nIs num > 5? I predict True.")
print(num > 5)
print("\nIs num < 5? I predict False.")
print(num < 5)
print("\nIs num >= 10? I predict True.")
print(num >= 10)
print("\nIs num <= 9? I predict False.")
print(num <= 9)
age = 20
has_id = True
print("\nIs age > 18 and has_id == True? I predict True.")
print(age > 18 and has_id == True)
print("\nIs age > 18 and has_id == False? I predict False.")
print(age > 18 and has_id == False)
print("\nIs age < 18 or has_id == True? I predict True.")
print(age < 18 or has_id == True)
print("\nIs age < 18 or has_id == False? I predict False.")
print(age < 18 or has_id == False)
colors = ['red', 'blue', 'green']
print("\nIs 'red' in colors? I predict True.")
print('red' in colors)
print("\nIs 'green' in colors? I predict False.")
print('green' in colors)
print("\nIs 'green' not in colors? I predict True.")
print('green' not in colors)
print("\nIs 'blue' not in colors? I predict False.")
print('blue' not in colors)
#5.3
alien_color = 'green'
if alien_color == 'green':
    print("You just earned 5 points!")
alien_color = 'red'

if alien_color == 'green':
    print("You just earned 5 points!")
#5.4
alien_color = 'green'
if alien_color == 'green':
    print("You just earned 5 points for shooting the alien.")
else:
    print("You just earned 10 points.")
alien_color = 'yellow'

if alien_color == 'green':
    print("You just earned 5 points for shooting the alien.")
else:
    print("You just earned 10 points.")
#5.5
alien_color = 'green' 

if alien_color == 'green':
    print("You earned 5 points.")
elif alien_color == 'yellow':
    print("You earned 10 points.")
elif alien_color == 'red':
    print("You earned 15 points.")
#5.6
age = 25

if age < 2:
    print("The person is a baby.")
elif 2 <= age < 4:
    print("The person is a toddler.")
elif 4 <= age < 13:
    print("The person is a kid.")
elif 13 <= age < 20:
    print("The person is a teenager.")
elif 20 <= age < 65:
    print("The person is an adult.")
else:
    print("The person is an elder.")
#5.7
favorite_fruits = ['apple', 'cherries', 'avacado']
if 'cherries' in favorite_fruits:
    print("You really like cherries!")
if 'apple' in favorite_fruits:
    print("You really like apples!")
if 'orange' in favorite_fruits:
    print("You really like oranges!")
if 'avacado' in favorite_fruits:
    print("You really like avacados!")
if 'grape' in favorite_fruits:
    print("You really like grapes!")
#5.8
usernames = ['admin', 'Lexi', 'Gabby', 'Emma', 'Olivia']
for user in usernames:
    if user == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {user}, thank you for logging in again.")
#5.9
usernames = [] 

if usernames:
    for user in usernames:
        if user == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {user}, thank you for logging in again.")
else:
    print("We need to find some users!")
#5.10
current_users = ['Lexi', 'Gabby', 'Emma', 'Lana', 'Caitlin']
new_users = ['lexi', 'Dane', 'Leah', 'Grace', 'Chris']
current_users_lower = [user.lower() for user in current_users]
for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Sorry {new_user}, that username is taken. Please enter a new username.")
    else:
        print(f"Great, the username {new_user} is available.")
#5.11
numbers = list(range(1, 10))
for num in numbers:
    if num == 1:
        suffix = 'st'
    elif num == 2:
        suffix = 'nd'
    elif num == 3:
        suffix = 'rd'
    else:
        suffix = 'th'
    print(f"{num}{suffix}")
#5.12
if alien_color == 'green':
    print("You earned 5 points/")
elif alien_color == 'yellow':
    print("You earned 10 points/")
else:
    print("You earned 15 points/")
#5.13
# I would consider programming a survey for social media users 