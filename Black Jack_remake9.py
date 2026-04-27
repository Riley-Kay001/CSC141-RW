import pygame
import pywidgets
import random
import sys

pygame.init()

# Window
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Higher Lower")

WHITE = (255, 255, 255)


# Deck class
class Deck:
    def __init__(self):
        self.cards = []
        values = [2,3,4,5,6,7,8,9,10,10,10,10,11]  # J,Q,K=10, Ace=11
        for value in values * 4:
            self.cards.append(Card(value))
        random.shuffle(self.cards)

    def dealCard(self):
        return self.cards.pop()

class Game:
    def __init__(self, window):
        self.window = window
        self.deck = Deck()
        self.currentCard = self.deck.dealCard()
        self.nextCard = None
        self.message = "Click Higher or Lower"

    def reset(self):
        self.deck = Deck()
        self.currentCard = self.deck.dealCard()
        self.message = "New Game Started"

    def hitHigherOrLower(self, guess):
        self.nextCard = self.deck.dealCard()

        if (guess == "HIGHER" and self.nextCard.getValue() >= self.currentCard.getValue()) or \
           (guess == "LOWER" and self.nextCard.getValue() <= self.currentCard.getValue()):
            self.message = "Correct!"
            self.currentCard = self.nextCard
            return False
        else:
            self.message = "Wrong! Game Over"
            return True

    def draw(self):
        font = pygame.font.SysFont(None, 48)

        text = font.render(f"Current Card: {self.currentCard.getValue()}", True, WHITE)
        self.window.blit(text, (350, 200))

        msg = font.render(self.message, True, WHITE)
        self.window.blit(msg, (350, 300))

# Screen
background = pywidgets.Image(window, (0, 0),
                          'images/background.png')
newGameButton = pywidgets.TextButton(window, (20, 530), 
                                  'New Game', width=100, height = 45)
higherButton = pywidgets.TextButton(window, (540, 520),
                                    'Higher', width= 120, height = 55)
lowerButton = pywidgets.TextButton(window, (340, 520),
                                   'Lower', width = 120, height = 55)
quitButton = pywidgets.TextButton(window, (880, 530),
                                  'Quit', width = 100, height = 45)

oGame = Game(window)

while True:
    for event in pygame.event.get():
        if ((event.type == QUIT) or
            ((event.type == KEYDOWN) and (event.key == K_ESCAPE)) or
            (quitButton.handleEvent(event))):
            pygame.quit()
            sys.exit

        if newGameButton.handleEvent(event):
            oGame.rest()
            lowerButton.enable()
            higherButton.enable()

        if higherButton.handleEvent(event):
            gameOver = oGame.hitHigherOrLower(HIGHER)
            if gameOver:
                higherButton.disable()
                lowerButton.disable()

        if lowerButton.handleEvent(event):
            gameOver = oGame.hitHigherOrLower(LOWER)
            if gameOver:
                higherButton.disable()
                lowerButton.disable()


    # Draw everything
    background.draw()
    oGame.draw()

    newGameButton.draw()
    higherButton.draw()
    lowerButton.draw()
    quitButton.draw()

    pygame.display.update()