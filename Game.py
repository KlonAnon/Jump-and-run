import pygame
pygame.init()

#class for the player
class Player():
    def __init__(self, width, height, x, y):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.surf = pygame.Surface((self.width, self.height))
        self.vel = 10
        self.isJumping = False
        self.jumpVelocity = 10

    def draw(self):
        window.blit(self.surf, (self.x, self.y))

    def move(self, direction):
        if direction == "left":
            self.x -= self.vel
        if direction == "right":
            self.x += self.vel

    def jump(self):
        if self.jumpVelocity >= -10:
            multiplier = 1 
            if self.jumpVelocity < 0:
                multiplier = -1
            self.y -= self.jumpVelocity ** 2 // 2 * multiplier
            self.jumpVelocity -= 1
        else:
            self.jumpVelocity = 10
            self.isJumping = False

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
    player.draw()
    pygame.display.flip()

#creating the player instance
player = Player(50, 50, 50, 300)

#creating the displayed window
win_width, win_height = 1000, 600
window = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Jump and run")

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
    
