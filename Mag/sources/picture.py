import pygame
from pygame.locals import *

class Picture:
	directory = "assets"
	def __init__(self, mag, file, pos):
		self.Mag = mag
		self.dir = dir
		self.file = file
		self.pos = pos
		self.Mag.scene.add(self)

	def draw(self):
		pygame.draw.rect(Mag.screen, WHITE, (50, 20, 120, 100))