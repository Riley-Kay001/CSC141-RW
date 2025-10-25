#8 - 1 Display Message
def display_message():
    print("This chapter we will be learning about functions, which are named blocks of code.")
display_message()

#8 - 2 Favorite Book
def favorite_book(title):
    print(f"One of my favorite books is {title}.")
favorite_book("Nancy Drew")
favorite_book("Judy Bloom")
favorite_book("The Outsiders")

#8 - 3 T-Shirts
def make_shirt(message, size):
    print(f"You made a size {size} with it saying {message}")
make_shirt("Good Morning", "medium") 
make_shirt("Coco-Cola ", "Large")

#8 - 4 Large Shirts
def make_shirt(size = "Small", message = "LIVE, LAUGH, LOVE"):
    print(f"I am making a size {size} T-shirt saying {message}")
make_shirt()
make_shirt(size = "medium")
make_shirt("Baby Tee", "Rock On")

#8 - 5 Cities
def describe_city(city, country = "USA"):
    print(f"{city} is in {country}")
describe_city("New York")
describe_city("Los Angelas")
describe_city ("Tokoyo")

#8 - 6 City Names
def city_country(city, country):
    return f"{city}, {country}"
print (city_country("Santorini", "Greece"))
print (city_country("Vancouver","Canada"))
print (city_country("Rome", "Italy"))

#8 - 7 Albums
def make_album(artist, title, songs = None):
    album = {'artist': artist, 'title': title}
    if songs is not None:
        album ['songs'] = songs
    return album
album1 = make_album("Views", "Drake")
album2 = make_album("SZA", "SOS")
album3 = make_album("The Strokes", "The New Albronmal")

print(album1)
print(album2)
print(album3)

album4 = make_album ("Drake", "Certified Lover Boy", songs = 5)
print(album4)
#8 - 8 User Albums
def make_album(artist, title, songs = None):
    album = { 'Artist' : artist , 
             'title' : title}
    if songs is not None:
        album ['songs'] = songs
    return album

print ("\nEnter 'q' at any time to quit.")

#while True:
    #artist = input("Enter the artist's name: ")
    #if artist.lower() == 'q':
        #break

    #title = input("Enter the ablum title: ")
    #if title.lower() == 'q':
        #break
    
    #song_input = input("Enter the number of songs (or press Enter)")
    #if songs_input.lower() == 'q':
        #break

    #if song_input:
        #album = make_album(artist, title, songs=int(songs_input))
    #else: 
        #album = make_album(artist, title)

    #print("Album created:" , album)

#8 - 9 Messages
def show_messages(messages):
    for message in messages:
        print(message)

messages = ["Hello!", "I am on my way!", "Let's meet at Jakes!", "Is everything okay?"]
show_messages(messages)

#8 - 10 Sending Messages
def show_messages(messages):
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop(0)
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)

messages = ["Hello!", "I am on my way!", "Let's meet at Jakes!", "Is everything okay?"]
sent_messages = []

send_messages(messages, sent_messages)

print("\nFinal Lists:")
print("Messages: ", messages)
print("Sent Messages: ", sent_messages)

#8 - 11 Archieved Messages 
def send_messages(mnessages, sent_messages):
    while messages:
        current_message = messages.pop(0)
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)
original_messages = ["Hello!", "I am on my way!", "Let's meet at Jakes!", "Is everything okay?"]
sent_messages = []

send_messages(original_messages[:], sent_messages)

print("\nOriginal Messages (should be unchanged):", original_messages)
print("Sent Messages: ", sent_messages)

#8 - 12 Sandwiches
def make_sandwich(*items):
    print("\nMaking a sandwich with the following items:")
    for item in items:
        print(f"- {item}")
make_sandwich('turkey', 'lettuce', 'tomato')
make_sandwich("peanut butter", "jelly")
make_sandwich("meatball", "Provolone", "olives")

#8 - 13 User Profile
def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

my_profile = build_profile('Riley Kay', 'Winchell', 
    location = 'Reading',
    profession = 'college student',
    hobby = 'softball',
    affiliations = 'ADPi')
print(my_profile)

#8 - 14 Cars
def make_car(manufacturer, model, **options):
    cars = {'maufacturer' : manufacturer,
            'model' : model}
    for key, value in options.items():
        cars[key] = value
    return cars

cars = make_car('suburu', 'outback', color = 'red', tow_package = True)

print(cars)