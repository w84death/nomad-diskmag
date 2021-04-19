import pygame
from pygame.locals import *
import time
import math

class Clipart:
	def __init__(self, mag, clip, pos, transparent="white", palette=()):
		self.Mag = mag
		self.clip = clip
		self.pos = pos
		self.transparent = transparent
		self.palette = palette
		self.Mag.scene.add(self)

	def draw(self):
		if self.clip == 'cover_0':
			self.draw_cover_0(self.pos)
		if self.clip == 'floppy':
			self.draw_floppy(self.pos)
	
	def draw_cover_0(self, pos):
		x = self.pos[0]
		y = self.pos[1] - 80 + math.sin(time.time()) * 80
		
		drive_x = self.pos[0] - 4
		drive_y = self.pos[1] - 30

		btn_x = drive_x + 170
		btn_y = drive_y

		

		pygame.draw.rect(self.Mag.screen, Color("#dddddd"), (drive_x-28, drive_y+20, 240, 10))
		pygame.draw.rect(self.Mag.screen, Color("#cccccc"), (drive_x-28, drive_y-20, 240, 40))

		pygame.draw.rect(self.Mag.screen, Color("#222222"), (drive_x, drive_y, 164, 14))
		pygame.draw.rect(self.Mag.screen, Color("#eeeeee"), (drive_x, drive_y+12, 164, 2))

		self.draw_floppy((x,y))

		pygame.draw.rect(self.Mag.screen, Color("#222222"), (drive_x, drive_y, 164, 2))
		pygame.draw.rect(self.Mag.screen, Color("#cccccc"), (drive_x-28, drive_y-20, 240, 20))
		pygame.draw.rect(self.Mag.screen, Color("#eeeeee"), (drive_x-28, drive_y-170, 240, 150))
		pygame.draw.rect(self.Mag.screen, Color("#222222"), (btn_x, btn_y, 20, 12))

	def draw_floppy(self, pos):
		x = pos[0]
		y = pos[1]
		if len(self.palette) > 0:
			p = self.palette
		else:
			p = ("#b21cb0", "#e532e2", "#e5b7e4")

		pygame.draw.rect(self.Mag.screen, Color(p[0]), (x+4, y+4, 152, 160))
		pygame.draw.rect(self.Mag.screen, Color(p[1]), (x, y, 152, 160))
		pygame.draw.rect(self.Mag.screen, Color("#eaeaea"), (x+(152*0.5-40), y, 80, 50))
		pygame.draw.rect(self.Mag.screen, Color(p[1]), (x+84, y+7, 21, 40))
		pygame.draw.rect(self.Mag.screen, Color(p[0]), (x+5, y+142, 8, 8))
		pygame.draw.rect(self.Mag.screen, Color(p[0]), (x+139, y+142, 8, 8))
		pygame.draw.rect(self.Mag.screen, Color(self.transparent), (x+141, y+144, 6, 6))
		pygame.draw.rect(self.Mag.screen, Color(p[2]), (x+20, y+67, 110, 94))
		