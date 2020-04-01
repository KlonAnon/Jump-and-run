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

    if not paused:
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT]:
            player.move("left")
        if keys[pygame.K_RIGHT]:
            player.move("right")

        if not player.isJumping:
            if keys[pygame.K_SPACE]:
                player.isJumping = True
                player.jump()
        if player.isJumping:
            player.jump()
            
#function for updating the displayed window
def window_updater(player): 
    window.fill(white)
    player.draw(window)
    pygame.display.flip()

#creating the displayed window
win_width, win_height = 1000, 600
window = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Jump and run")

#creating the player instance
player = Player()

#color variables
white = (255, 255, 255)

#game flow variables           
running = True
paused = False

#main game loop 
while running:
    pygame.time.wait(25)
    
    event_handler()
    player_handler(player)
    window_updater(player)

#quit everything
pygame.quit()
    
