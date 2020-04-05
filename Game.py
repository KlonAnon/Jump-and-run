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
def key_handler(player):
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
            enemyList.append(Enemy(50,50,1000,300,8))
        for enemy in enemyList:
            enemy.move_left()
            if enemy.x + enemy.width <= 0:
                enemyList.clear()
            
#function for updating the displayed window
def window_updater(player): 
    for graphic in graphics:
        if isinstance(graphic, list):
            for index in graphic:
                index.draw(window)
        else:
            graphic.draw(window)
    pygame.display.flip()

#creating the displayed window
win_width, win_height = 1000, 600
window = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Jump and run")

#creating necessary objects
player = Player(width=50, height=50, x=win_width//2, y=300, vel=10)
bg1 = Background(win_width, win_height, x=0, y=0, vel=10, img="bg-1.png")
bg2 = Background(win_width, win_height, x=win_width, y=0, vel=10, img="bg-1.png")
backgrounds = [bg1, bg2]
enemyList = []
graphics = [backgrounds, enemyList, player]

#game flow variables           
running = True
paused = False

#main game loop 
while running:
    pygame.time.wait(25)
    
    BasicEvent_handler()
    if not paused:
        key_handler(player)
        #enemy_func(enemyList)
    window_updater(player)

#quit everything
pygame.quit()
