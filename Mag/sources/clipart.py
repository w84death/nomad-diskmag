import pygame
from pygame.locals import *
import time
import math

class Clipart:
    def __init__(self, mag, clip, pos):
        self.Mag = mag
        self.clip = clip
        self.pos = pos
        self.Mag.scene.add(self)

    def draw(self):
        if self.clip == 'floppy':
            self.draw_floppy()
    
    def draw_floppy(self):
        x = self.pos[0]
        y = self.pos[1] - 40 + math.sin(time.time()) * 80
        
        drive_x = self.pos[0] - 4
        drive_y = self.pos[1] - 30

        btn_x = drive_x + 170
        btn_y = drive_y

        pygame.draw.rect(self.Mag.screen, Color("#222222"), (drive_x, drive_y, 164, 14))
        pygame.draw.rect(self.Mag.screen, Color("#eeeeee"), (drive_x, drive_y+12, 164, 2))

        pygame.draw.rect(self.Mag.screen, Color("#b21cb0"), (x+4, y+4, 152, 160))
        pygame.draw.rect(self.Mag.screen, Color("#e532e2"), (x, y, 152, 160))
        pygame.draw.rect(self.Mag.screen, Color("#eaeaea"), (x+(152*0.5-40), y, 80, 50))
        pygame.draw.rect(self.Mag.screen, Color("#e532e2"), (x+84, y+7, 21, 40))
        pygame.draw.rect(self.Mag.screen, Color("#b21cb0"), (x+5, y+142, 8, 8))
        pygame.draw.rect(self.Mag.screen, Color("#ccc39d"), (x+139, y+142, 8, 8))
        pygame.draw.rect(self.Mag.screen, Color("#e5b7e4"), (x+20, y+67, 110, 94))


        pygame.draw.rect(self.Mag.screen, Color("#222222"), (drive_x, drive_y, 164, 2))
        pygame.draw.rect(self.Mag.screen, Color("#ccc39d"), (drive_x, drive_y-180, 164, 180))
        pygame.draw.rect(self.Mag.screen, Color("#222222"), (btn_x, btn_y, 20, 12))
        

        
        