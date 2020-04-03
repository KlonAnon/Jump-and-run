import pygame
pygame.init()

#superclass for game graphics
class GameGraphics():
    def __init__(self, width, height, x, y, vel, img = None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.vel = vel

        if img != None:
            self.graphic = pygame.transform.scale(pygame.image.load(img), (self.width, self.height))
        else:
            self.graphic = pygame.Surface((self.width, self.height))

    def draw(self, window):
        window.blit(self.graphic, (self.x, self.y))

    def move_left(self):
        self.x -= self.vel

    def move_right(self):
        self.x += self.vel
    
#class for the player
class Player(GameGraphics):
    def __init__(self, width, height, x, y, vel, img = None):
        super().__init__(width, height, x, y, vel, img)
        
        self.isJumping = False
        self.jumpVelocity = 10

    def window_boundaries(self, window):   
        if self.x <= 0:
            self.x = 0
        elif self.x >= window.get_width() - self.width:
            self.x = window.get_width() - self.width 

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

#class for the enemy
class Enemy(GameGraphics):
    def __init__(self, width, height, x, y, vel, img = None):
        super().__init__(width, height, x, y, vel, img)
