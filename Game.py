from classes import *
import os.path 
import pygame
pygame.init()

#function for basic event handling        
def basicEvent_handler():
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

        if paused:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    running = False

#function for handling the events of the player
def key_handler():
        keys = pygame.key.get_pressed()

        for graphic in grounds:
            if keys[pygame.K_LEFT]:
                graphic.move_right()
                for enemy in enemyList:
                    enemy.change_vel(enemy.normal_vel - grounds[0].vel)
                
            if keys[pygame.K_RIGHT]:
                graphic.move_left()
                for enemy in enemyList:
                    enemy.change_vel(enemy.normal_vel + grounds[0].vel)

            if not (keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]):
                graphic.isMoving_right = False
                graphic.isMoving_left = False
                for enemy in enemyList:
                    enemy.change_vel(enemy.normal_vel)
                
            graphic.reposition(window)

        if not player.isJumping:
            if keys[pygame.K_SPACE]:
                player.isJumping = True
                player.jump()
        if player.isJumping:
            player.jump()

#function for working with enemy objects (creating and removing)
def enemy_func(enemyList):
        if not len(enemyList) > 1:
            enemyList.append(Enemy(width=50,height=50,x=win_width,y=grounds[2].y - 50,vel=player.vel + 2))
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
win_width, win_height = 1920, 1080
window = pygame.display.set_mode((win_width, win_height), pygame.FULLSCREEN)
pygame.display.set_caption("Jump and run")


#creating necessary objects
    #list for all ground and background objects
grounds = []
    #background
for background in range(2):
    grounds.append(Background(win_width, win_height, x=win_width * background, y=0, vel=6,
                 img=os.path.join("images", "bg-1.png")))
    #ground
for ground in range(11):
    grounds.append(Ground(width= 192, height=192, x=192*ground, y=win_height - 192, vel=10,
                 img=os.path.join("images", "BottomGras.png")))
    #enemy
enemyList = []
    #player
player = Player(width=50, height=50, x=win_width//2, y=grounds[2].y - 50, vel=10)
    #graphics list
graphics = [grounds, enemyList, player]


#game flow variables           
running = True
paused = False

#main game loop 
while running:
    pygame.time.wait(25)
    
    basicEvent_handler()
    
    if not paused:
        key_handler()
        enemy_func(enemyList)

    window_draw(graphics)
    pygame.display.flip()

#quit everything
pygame.quit()
