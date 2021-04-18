import pygame
from pygame.locals import *

class Text():
    fontname = None
    fontsize = 24
    fontcolor = Color('black')
    background = None
    italic = False
    bold = False
    underline = False

    def __init__(self, mag, text, pos, size=24, color="black", align="left"):
        self.Mag = mag
        self.text = text
        self.pos = pos
        self.align = align
        self.fontname = None
        self.fontsize = size
        self.fontcolor = Color(color)
        self.set_font()
        self.render()
        self.Mag.scene.add(self)
    
    def set_font(self):
        self.font = pygame.font.Font(self.fontname, self.fontsize)

    def render(self):
        self.img = self.font.render(self.text, True, self.fontcolor)
        self.rect = self.img.get_rect()
        if self.align == "left":
            self.rect.topleft = self.pos
        if self.align == "center":
            self.rect.midtop = self.pos

    def draw(self):
        self.Mag.screen.blit(self.img, self.rect)