#
# Nomad Diskmag - CURSOR
# Rendering cursor
#
# E-zine on a 1.44 floppy tailored made on Raspberry Pi computer.
# Created by Krzysztof Krystian Jankowski
# https://krzysztofjankowski.com/nomad-diskmag
#

import pygame
from pygame.locals import *

class Cursor:
	def __init__(self, screen, pos, down=False):
		self.screen = screen
		self.pos = pos
		self.down = down
		self.step = 3
		self.palette = ["#222222", "#777777", "#cccccc"]

	def update(self, event):
		if event.type == pygame.MOUSEBUTTONDOWN:
			self.step = 1
		if event.type == MOUSEMOTION:
			self.pos = event.pos
		if event.type == pygame.MOUSEBUTTONUP:
			self.step = 2
		
	def update_palette(self, palette):
		self.palette = palette

	def draw(self):
		x, y = self.pos
		p = self.palette
		s = self.screen
		for l in range(len(self.palette)):
			xx = x - l*self.step+self.step
			yy = y - l*self.step+self.step
			pygame.draw.rect(s, Color(p[l]), (xx-4, yy, 8, 8))
			pygame.draw.rect(s, Color(p[l]), (xx-4, yy+8, 24, 16))
			pygame.draw.circle(s, Color(p[l]), (xx+8, yy+20), 12)
			pygame.draw.circle(s, Color(p[l]), (xx, yy), 4)
			pygame.draw.circle(s, Color(p[l]), (xx+8, yy+8), 4)
			pygame.draw.circle(s, Color(p[l]), (xx+14, yy+8), 4)
		
