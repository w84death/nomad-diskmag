#
# Raspberry Pi FDD Magazine
# 
# Magazine on a 1.44 floppy tailored for Raspberry Pi computers. 
# Created by Krzysztof Krystian Jankowski
# https://krzysztofjankowski.com/pifddmag
#
import pygame
from pygame.locals import *
from chapter import Chapter
from text import Text
from picture import Picture
from scene import Scene
from clipart import Clipart

class Mag:
    resolution = (0,0)
    scenes = []
    current_scene = 0
    shortcuts = {
        K_1: 'self.change_scene(0)',
        K_2: 'self.change_scene(1)',
        K_n: 'self.next_scene()',
        K_m: 'self.change_page()',
        K_ESCAPE: 'self.quit()',
    }
    running = True
    drawing = False

    def __init__(self, resolution, caption, chapters):
        pygame.init()
        flags = NOFRAME
        Mag.resolution = resolution
        Mag.screen = pygame.display.set_mode(resolution)
        pygame.display.set_caption(caption)
        Mag.chapter = Chapter(chapters)
        

    def do_shortcut(self, event):
        k = event.key
        m = event.mod 
        
        if k in self.shortcuts:
            exec(self.shortcuts[k])

    def change_scene(self, scene_id):
        self.scene = self.scenes[scene_id]
        pygame.display.set_caption(self.scene.caption)  

    def change_page(self):
        self.scene.paginator.change_page()

    def next_scene(self):
        self.current_scene += 1
        if self.current_scene > len(self.scenes) - 1:
                self.current_scene = 0
        self.change_scene(self.current_scene)

    def go_next_virtual_page(self):
        if not self.scene.paginator.change_page():
            self.next_scene()

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
                elif event.type == MOUSEBUTTONDOWN:
                    self.go_next_virtual_page()   
            if self.drawing:
                self.scene.draw()
        pygame.quit()

if __name__ == '__main__':
    Mag(resolution=(480,640), caption="Main").loop()