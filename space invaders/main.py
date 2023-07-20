import pygame
import math
import random
from pygame import mixer

#intialize pygame
pygame.init()

# create window
screen = pygame.display.set_mode((800, 600)) # create the screen in px
pygame.display.set_caption("space Invaders") # sets the title
pygame.display.set_icon(pygame.image.load("ufo.png")) # sets the icon

#background sound
mixer.music.load("background.wav")
mixer.music.play(-1) # so it will play infinitely

#player
playerImg = pygame.image.load("player.png")
playerCordX = 370
playerCordY = 480
playerX_change = 0

#enemy
enemyImg = []
enemyCordX = []
enemyCordY = []
enemyX_change = []
enemyY_change = []
num_enemy = 6

for i in range(num_enemy):
    enemyImg.append(pygame.image.load("monster.png"))
    enemyCordX.append(random.randint(0, 735))
    enemyCordY.append(random.randint(50, 150))
    enemyX_change.append(4)
    enemyY_change.append(40)

#bullet 
bulletImg = pygame.image.load("bullet.png")
bulletCordX = 0 
bulletCordY = 480
bulletY_change = 20
bullet_state = "ready"

#score
score = 0
font = pygame.font.Font("freesansbold.ttf", 32)
textX = 10
textY = 10

#gameover
fontGameover = pygame.font.Font("freesansbold.ttf", 64)

# functions
def player(x, y):
    screen.blit(playerImg, (x, y)) # blit mean draw

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x+16, y+10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow((enemyX-bulletX),2))+(math.pow((enemyY-bulletY),2)))
    if distance < 27:
        return True
    else:
        return False
def show_score(x, y):
    score_view = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_view, (x, y))

def show_game_over():
    over_text = font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (290, 270))

# game loop
running = True
while running:
    # changing the background color
    # screen.fill((0,0,0))
    # background image
    screen.blit(pygame.image.load("background.png"), (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # if the window's x is pressed the main loop will be closed
            running = False
            
        # movement on keystroke
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletCordX = playerCordX
                    fire_bullet(bulletCordX, bulletCordY)
                    mixer.Sound("laser.wav").play()
        if event.type == pygame.KEYUP:
            playerX_change = 0


    playerCordX += playerX_change 

    # add boundaries for our player and enemy    so it doesn't go outside
    if playerCordX <= 0:
        playerCordX = 0
    elif playerCordX >= 736:
        playerCordX = 736

    
    for i in range(num_enemy):
        #Game over
        if enemyCordY[i] > 440:
            for j in range(num_enemy):
                enemyCordY[j] = 2000
            show_game_over()
            mixer.music.stop()
            break

        enemyCordX[i] += enemyX_change[i]
        
        if enemyCordX[i] <= 0:
            enemyX_change[i] = 4
            enemyCordY[i] += enemyY_change[i]
        elif enemyCordX[i] >= 736:
            enemyX_change[i] = -4
            enemyCordY[i] += enemyY_change[i]

        # collision
        collision = isCollision(enemyCordX[i], enemyCordY[i], bulletCordX, bulletCordY)
        if collision:
            mixer.Sound("explosion.wav").play()
            bulletCordY = 480
            bullet_state = "ready"
            score += 1
            enemyCordX[i] = random.randint(0, 735)
            enemyCordY[i] = random.randint(50, 150)

        #shows the enemy at the selected coordinates
        enemy(enemyCordX[i], enemyCordY[i], i)

    # Bullet movement
    if bulletCordY <= 0:
        bulletCordY = 480
        bullet_state = "ready"
    if bullet_state is "fire":
        fire_bullet(bulletCordX, bulletCordY)
        bulletCordY -= bulletY_change

    # shows the player at the selected coordinates
    player(playerCordX, playerCordY)

    # show score
    show_score(textX, textY)

    # update after every change otherwise it won't show on the screen
    pygame.display.update()