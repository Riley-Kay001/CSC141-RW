# 1 - Import packages
import pygame
from pygame.locals import *
import sys
import random
from math import sin 

# Ball class
class Ball():
    def __init__(self, window, windowWidth, windowHeight):
        self.window = window # remember the window, so we can draw later
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight
        self.image = pygame.image.load('images/ball.png')

# A rect is made up of [x, y, width, height]
        self.ballRect = self.image.get_rect()
        self.width = self.ballRect.width
        self.height = self.ballRect.height
        self.maxWidth = windowWidth - self.width
        self.maxHeight = windowHeight - self.height

# Pick a random starting position
        self.x = random.randrange(0, self.maxWidth)
        self.y = self.height

# Choose a random speed between -4 and 4, but not zero
# in both the x and y directions
        speedsList = [-7, -6, -5, -4, -3, 3, 4, 5, 6, 7]
        self.xSpeed = random.choice(speedsList)
        self.ySpeed = random.randrange(self.maxHeight, self.windowHeight * 2)
    def update(self):

# Check for hitting a wall. If so, change that direction.
        if (self.x < -self.width) or (self.x >= self.windowWidth):
            self.xSpeed = -self.xSpeed

# Update the Ball's x and y, using the speed in two directions
        self.x = self.x + self.xSpeed
        self.y = self.windowWidth - self.ySpeed * sin(3.14 * self.x /self.maxWidth)
        self.ballRect.x = self.x
        self.ballRect.y = self.y
        self.rect = self.image.get_rect()
    def draw(self):
        self.window.blit(self.image, (self.x, self.y))

# 2 - Define constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30 
       
# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("The Ball Clicker Game")
clock = pygame.time.Clock()  

# 4 - Load assets: image(s), sounds, etc.
font = pygame.font.SysFont(None, 48)

# 5 - Initialize variables
ballList = []
score = 0
lastSeconds = 0
startTicks = pygame.time.get_ticks()
oBall = Ball(window, WINDOW_WIDTH, WINDOW_HEIGHT)
gameOver = False

# 6 - Loop forever
while True:
    
    seconds = (pygame.time.get_ticks() - startTicks)// 1000

    # 7 - Check for and handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()    

    if event.type == pygame.MOUSEBUTTONDOWN and not gameOver:
        mousePos = pygame.mouse.get_pos()
        for ball in ballList[:]:
            if ball.rect.collide(mousePos):
                 ballList.remove(ball)
                 score += 1
        if not gameOver:

            if gameOver:
                gameOverText = font.render("Game Over!", True, (255, 255, 255))
                window.blit(gameOverText, (150, 220))

    # 8 - Do any "per frame" actions
        seconds = (pygame.time.get_ticks() - startTicks) // 1000

        # Add a new ball every second
    if seconds > lastSeconds:
        ballList.append(Ball (window, WINDOW_WIDTH, WINDOW_HEIGHT))
        lastSrconds = seconds

    # End the game after 15 seconds
    if seconds >= 15:
        gameOver = True
        ballList.clear()

    for ball in ballList:
        oBall.update()  # tell the Ball to update itself

   # 9 - Clear the window before drawing it again
    window.fill(BLACK)
    
    # 10 - Draw the window elements
    for ball in ballList:
        oBall.draw()   # tell the Ball to draw itself

    scoreText = font.render(f"Score: {score}", True, WHITE)
    window.blit(scoreText, (10, 10))

    secondsText = font.render(f"Game Over! Final Score: {score}", True, WHITE)
    window.blit(gameOverText, (150, 220))


    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make pygame wait
