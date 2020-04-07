from classes import *
import pygame
pygame.init()

#function for basic event handling        
def BasicEvent_handler():
    global running
    global paused
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if paused == False:
                    paused = True
                elif paused == True:
                    paused = False

#function for handling the events of the player
def key_handler():
        keys = pygame.key.get_pressed()

        for background in backgrounds:
            if keys[pygame.K_LEFT]:
                background.move_right()
            if keys[pygame.K_RIGHT]:
                background.move_left()

            background.reposition()

        if not player.isJumping:
            if keys[pygame.K_SPACE]:
                player.isJumping = True
                player.jump()
        if player.isJumping:
            player.jump()

#function for working with enemy objects (creating and removing)
def enemy_func(enemyList):
        if not len(enemyList) > 1:
            enemyList.append(Enemy(50,50,1000,300,15))
        for enemy in enemyList:
            enemy.move_left()
            if enemy.x + enemy.width <= 0:
                enemyList.clear()
            
#function for updating the displayed window
def window_draw(graphics): 
    for graphic in range(len(graphics)):
        try:
            graphics[graphic].draw(window)
        except:
            window_draw(graphics[graphic])
            window_draw(graphics[1 + graphic:])
        
#creating the displayed window
win_width, win_height = 1000, 600
window = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Jump and run")

#creating necessary objects
player = Player(width=50, height=50, x=win_width//2, y=300, vel=10)
bg1 = Background(win_width, win_height, x=0, y=0, vel=8, img="bg-1.png")
bg2 = Background(win_width, win_height, x=win_width, y=0, vel=8, img="bg-1.png")
backgrounds = [bg1, bg2]
ground = Ground(width= 500, height=250, x=0, y=350, vel=10, img="BottomGras.png")
ground2 = Ground(width= 500, height=250, x=500, y=350, vel=10, img="BottomGras.png")
grounds = [ground, ground2]
enemyList = []
graphics = [backgrounds, grounds, enemyList, player]

#game flow variables           
running = True
paused = False

#main game loop 
while running:
    pygame.time.wait(25)
    
    BasicEvent_handler()
    if not paused:
        key_handler()
        enemy_func(enemyList)
    window_draw(graphics)
    pygame.display.flip()

#quit everything
pygame.quit()
