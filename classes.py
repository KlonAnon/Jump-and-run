import pygame
pygame.init()

#class for the player
class Player():
    def __init__(self):
        self.width = 50
        self.height = 50
        self.x = 50
        self.y = 300
        self.surf = pygame.Surface((self.width, self.height))
        self.vel = 10
        self.isJumping = False
        self.jumpVelocity = 10

    def draw(self, window):
        window.blit(self.surf, (self.x, self.y))

    def move(self, direction, window):
        if direction == "left":
            self.x -= self.vel
        if direction == "right":
            self.x += self.vel
            
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
class Enemy():
    def __init__(self):
        self.width = 50
        self.height = 50
        self.x = 1000
        self.y = 300
        self.surf = pygame.Surface((self.width, self.height))
        self.vel = 8

    def draw(self, window):
        window.blit(self.surf, (self.x, self.y))

    def move(self):
        self.x -= self.vel
