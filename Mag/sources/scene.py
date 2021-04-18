import pygame
from pygame.locals import *

class Scene:
    id = 0
    bg = Color('white')

    def __init__(self, mag, text, caption="Window Caption", title="Scene Title", bg="white", color="black", align="left"):
        self.Mag = mag
        self.Text = text
        self.Mag.scenes.append(self)
        self.Mag.scene = self
        self.id = Scene.id
        Scene.id += 1
        self.nodes = []
        self.bg = Color(bg)
        self.caption = caption
        aligned_pos = (0,12)
        if align == "center":
            aligned_pos = (self.Mag.resolution[0] * 0.5, 12)
        self.add(self.Text(self.Mag, title, size=40, pos=aligned_pos, align=align, color=color, column_limit=30))

    def draw(self):
        self.Mag.screen.fill(self.bg)
        for node in self.nodes:
            node.draw()
        pygame.display.flip()

    def add(self, element):
        self.nodes.append(element)
    
    def __str__(self):
        return 'Scene {}'.format(self.id)

    def show(self):
        self.Mag.scene = self