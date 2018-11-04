import pygame
import sys
from pygame.locals import *


class Ball(object):
    def __init__(self, x, y, vx, vy, radius, colour):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.radius = radius
        self.colour = colour

    def move(self):
        self.x += self.vx
        self.y += self.vy

    def draw(self, surface):
        pygame.draw.circle(surface, self.colour, (self.x, self.y), self.radius, 0)

    def rect(self):
        return pygame.Rect(self.x - self.radius, self.y - self.radius, 2 * self.radius, 2 * self.radius)


class Paddle(object):
    def __init__(self, x, y, width, height, colour):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vy = 0
        self.colour = colour

    def draw(self, screen):
        pygame.draw.rect(screen, self.colour, self.rect())

    def move(self):
        self.y += self.vy

    def rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)


class Game(object):
    WHITE = (255, 255, 255)
    BLACK = (0,   0,   0)

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((500, 300))
        self.ball = Ball(250, 150, 3, 3, 10, Game.BLACK)
        self.left_bat = Paddle(0, 125, 20, 50, Game.BLACK)
        self.right_bat = Paddle(480, 125, 20, 50, Game.BLACK)

    def play(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            self.draw()

    def draw(self):
        self.screen.fill(Game.WHITE)
        self.ball.draw(self.screen)
        self.left_bat.draw(self.screen)
        self.right_bat.draw(self.screen)
        pygame.display.update()


if __name__ == "__main__":
    Game().play()