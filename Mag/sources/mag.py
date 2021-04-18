#
# Raspberry Pi FDD Magazine
# 
# Magazine on a 1.44 floppy tailored for Raspberry Pi computers. 
# Created by Krzysztof Krystian Jankowski
# https://krzysztofjankowski.com/pifddmag
#

import pygame
from pygame.locals import *

class Text:
    def __init__(self, text, pos, size=24, color='black', **options):
        self.text = text
        self.pos = pos

        self.fontname = None
        self.fontsize = size
        self.fontcolor = Color(color)
        self.set_font()
        self.render()
        Mag.scene.add(self)
    
    def set_font(self):
        self.font = pygame.font.Font(self.fontname, self.fontsize)

    def render(self):
        self.img = self.font.render(self.text, True, self.fontcolor)
        self.rect = self.img.get_rect()
        self.rect.topleft = self.pos

    def draw(self):
        Mag.screen.blit(self.img, self.rect)

class Picture:
    directory = "assets"
    def __init__(self, file, pos):
        self.dir = dir
        self.file = file
        self.pos = pos
        self.render()
        Mag.scene.add(self)

    def render(self):
        self.img = pygame.image.load("{dir}/{file}".format(dir=self.directory, file=self.file))
        self.img.convert()
        self.rect = self.img.get_rect()
        self.rect.center = self.pos

    def draw(self):
        Mag.screen.blit(self.img, self.rect) 

class Scene:
    id = 0
    bg = Color('white')

    def __init__(self, caption="Window Caption", title="Scene Title", bg="white"):
        Mag.scenes.append(self)
        Mag.scene = self
        self.id = Scene.id
        Scene.id += 1
        self.nodes = []
        self.bg = Color(bg)
        self.caption = caption
        self.add(Text(title, size=32, pos=(0,0)))

    def draw(self):
        Mag.screen.fill(self.bg)
        for node in self.nodes:
            node.draw()
        pygame.display.flip()

    def add(self, element):
        self.nodes.append(element)
    
    def __str__(self):
        return 'Scene {}'.format(self.id)

    def show(self):
        Mag.scene = self

class Mag:
    scenes = []
    shortcuts = {
        K_1: 'self.change_scene(0)',
        K_2: 'self.change_scene(1)',
        K_ESCAPE: 'self.quit()',
    }
    running = True
    drawing = False

    def __init__(self, resolution, caption):
        pygame.init()
        flags = NOFRAME
        Mag.screen = pygame.display.set_mode(resolution)
        pygame.display.set_caption(caption)

    def do_shortcut(self, event):
        k = event.key
        m = event.mod 
        
        if k in self.shortcuts:
            exec(self.shortcuts[k])

    def change_scene(self,scene_id):
        self.scene = self.scenes[scene_id]
        pygame.display.set_caption(self.scene.caption)       
            
    def quit(self):
        self.running = False

    def start_drawing(self):
        self.drawing = True
        
    def loop(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                if event.type == KEYDOWN:
                    self.do_shortcut(event)          
            if self.drawing:
                self.scene.draw()
        pygame.quit()

if __name__ == '__main__':
    Mag().loop()