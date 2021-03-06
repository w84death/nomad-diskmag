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
	deadzone = 0.1
	speed = 16
	def __init__(self, screen, pos, down=False):
		self.screen = screen
		self.pos = pos
		self.down = down
		self.step = 3
		
		self.palette = ["#222222", "#777777", "#cccccc"]

	def update(self, event):
		if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.JOYBUTTONDOWN:
			self.step = 1
		if event.type == MOUSEMOTION:
			self.pos = event.pos
		if event.type == pygame.MOUSEBUTTONUP or event.type == pygame.JOYBUTTONUP:
			self.step = 2
		
	def update_palette(self, palette):
		self.palette = palette

	def draw(self):
		x, y = self.pos
		p = self.palette
		s = self.screen
		for l in range(len(self.palette)):
			xx = int(x - l*self.step+self.step)
			yy = int(y - l*self.step+self.step)
			pygame.draw.polygon(s, Color(p[l]), [(xx, yy),(xx+12, yy+24),(xx+2,yy+20),(xx-8,yy+28)])

		
	def move(self, axis_x, axis_y):
		min_x = 12
		min_y = 12
		max_x = 1280-12
		max_y = 720-12
		x, y = self.pos
		if abs(axis_x) > self.deadzone:
			if axis_y < 0:
				x += (axis_x + self.deadzone) * self.speed 
			else:
				x += (axis_x - self.deadzone) * self.speed 
		if abs(axis_y) > self.deadzone:
			y += axis_y * self.speed

		if x < min_x: x = min_x
		if x > max_x: x = max_x
		if y < min_y: y = min_y
		if y > max_y: y = max_y
		self.pos = (x,y)

	def get_pos(self):
		return self.pos