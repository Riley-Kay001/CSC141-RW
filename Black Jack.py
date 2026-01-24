#The card deck
card_deck = [
    {'2' : 2},
    {'3' : 3},
    {'4' : 4},
    {'5' : 5},
    {'6' : 6},
    {'7' : 7},
    {'8' : 8},
    {'9' : 9},
    {'10' : 10},
    {'Jack' : 10},
    {'Queen' : 10},
    {'King' : 10},
    {'Ace' : [1,11]}
]


#Shuffling & Dealing Cards
import random

def shuffle_deck(deck):
    random.shuffle(deck)
    print(f"Shuffled list: {deck}")
    return deck

def deal_card(hand, deck):
    """Deals a single card from the deck to a player's hand. """
    if len(deck) > 0: 
        card = deck.pop()
        hand.append(card)
        return card
    else:
        return None 

def draw_card(deck):
    return deck.pop()


#Calculating score during the game 
def calculate_score(hand):
    score = 0
    aces = 0


    for card in hand:
        if card in ["J", "Q", "K"]:
            score += 10
        elif card == "A":
            score += 11
            aces += 1
        else:
            score += int(card)
    return score 


#Checking game status
def print_status(player_hand, dealers_hand, show_dealer_card=True):
    print("\nDealer's hand:")
    if show_dealer_card:
        print (dealer_hand)
    
    else:
        print([dealer_hand[0], "?"])
    
    print("Player's hand = ")
    print(player_hand)
    print("Player score = ", calculate_score(player_hand))

#Main Loop of the GAME
import random

def main():    
    deck =["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    random.shuffle(deck)

    dealer_hand = [draw_card(deck)]
    player_hand = [draw_card(deck), draw_card(deck)]

#Main Loop for Player's Turn
 #because player_hand was not identified
def setup():
    return "alive" 
player_hand = setup()
print(player_hand)


#because dealer_hand was not identified
def setup_dealer_hand():
    return "ready to play"
dealer_hand = setup_dealer_hand()
print(setup_dealer_hand)

while True:
    show_dealer_card=False
    print(player_hand, dealer_hand, show_dealer_card)
    if calculate_score(player_hand) > 21:
        print("You busted! Maybe next time. DEALER WINS!!")

    choice = input ("HIT or STAY? (h/s)").lower()
    if choice =="h":
    player_hand.append(draw_card(deck))

    else:
        score > 21
        print ("You Busted!!")
        

    while calculate_score(dealer_hand) < 17:
        dealer_hand.append(draw_card(deck))
    break

print_status(player_hand, dealer_hand, show_dealer_card)
player_score = calculate_score(player_hand)
dealer_score = calculate_score(dealer_hand)

if dealer_score > 21:
    print("Dealer busted! You win!")
elif dealer_score > player_score:
    print("Dealer wins!! Better luck next time.")
elif dealer_score < player_score:
    print("YOU WIN!! GREATTTT JOB!!")
else:
    print("It's a tie! Let's go again")


main()
    