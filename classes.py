import pygame

pygame.init()


# superclass for game graphics
class GameGraphics:
    def __init__(self, width, height, x, y, vel, img=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.vel = vel
        self.isMoving_right = False
        self.isMoving_left = False

        if img is not None:
            self.graphic = pygame.transform.scale(pygame.image.load(img), (self.width, self.height))
        else:
            self.graphic = pygame.Surface((self.width, self.height))

    def draw(self, window):
        window.blit(self.graphic, (self.x, self.y))

    def move_left(self):
        self.x -= self.vel
        self.isMoving_left = True
        self.isMoving_right = False

    def move_right(self):
        self.x += self.vel
        self.isMoving_right = True
        self.isMoving_left = False


# class for the player
class Player(GameGraphics):
    def __init__(self, width, height, x, y, vel, img=None):
        super().__init__(width, height, x, y, vel, img)

        self.isJumping = False
        self.jumpVelocity = 10
        self.isKilled = False

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

    def collision(self, graphic):
        if isinstance(graphic, Enemy):
            if self.isJumping:
                graphic.isKilled = True
            else:
                self.isKilled = True

        elif isinstance(graphic, Ground):
            if graphic.isMoving_right:
                self.x = graphic.x + graphic.width
            elif graphic.isMoving_left:
                self.x = graphic.x - self.width


# class for enemies
class Enemy(GameGraphics):
    def __init__(self, width, height, x, y, vel, img=None):
        super().__init__(width, height, x, y, vel, img)

        self.normal_vel = vel
        self.isKilled = False

    def change_vel(self, new_vel):
        self.vel = new_vel


# class for backgrounds
class Background(GameGraphics):
    def __init__(self, width, height, x, y, vel, img=None):
        super().__init__(width, height, x, y, vel, img)

    def reposition(self, window):
        if self.isMoving_left:
            if self.x <= -1 * self.width:
                self.x = window.get_width() + (self.x + self.width)

        elif self.isMoving_right:
            if self.x >= window.get_width():
                self.x = -1 * window.get_width() + (self.x - self.width)


# class for grounds
class Ground(Background):
    def __init__(self, width, height, x, y, vel, img=None):
        super().__init__(width, height, x, y, vel, img)
