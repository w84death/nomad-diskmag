import pygame
from pygame.locals import *

class Picture:
    directory = "assets"
    def __init__(self, mag, file, pos):
        self.Mag = mag
        self.dir = dir
        self.file = file
        self.pos = pos
        self.render()
        self.Mag.scene.add(self)

    def render(self):
        self.img = pygame.image.load("{dir}/{file}".format(dir=self.directory, file=self.file))
        self.img.convert()
        self.rect = self.img.get_rect()
        self.rect.center = self.pos

    def draw(self):
        self.Mag.screen.blit(self.img, self.rect)