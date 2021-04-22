#
# Nomad Diskmag - PICTURES
# Rendering rasterize graphics.
#
# E-zine on a 1.44 floppy tailored made on Raspberry Pi computer.
# Created by Krzysztof Krystian Jankowski
# https://krzysztofjankowski.com/nomad-diskmag
#

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