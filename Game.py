from classes import *
import pygame
pygame.init()

#function for basic event handling        
def event_handler():
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
def player_handler(player):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT]:
            bg1.move_right()
            bg2.move_right()
            for background in backgrounds:
                background.reposition_left()
        if keys[pygame.K_RIGHT]:
            bg1.move_left()
            bg2.move_left()
            for background in backgrounds:
                background.reposition_right()

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
    for background in backgrounds:
        background.draw(window)
    player.draw(window)
    for enemy in enemyList:
        enemy.draw(window)
    pygame.display.flip()

#creating the displayed window
win_width, win_height = 1000, 600
window = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Jump and run")

#creating necessary objects
player = Player(width=50, height=50, x=win_width//2, y=300, vel=10)
enemyList = []
bg1 = Background(win_width, win_height, x=0, y=0, vel=10, img="BG1.png")
bg2 = Background(win_width, win_height, x=win_width, y=0, vel=10, img="BG1.png")
backgrounds = [bg1, bg2]

#game flow variables           
running = True
paused = False

#main game loop 
while running:
    pygame.time.wait(25)
    
    event_handler()
    if not paused:
        player_handler(player)
        #enemy_func(enemyList)
    window_updater(player)

#quit everything
pygame.quit()
