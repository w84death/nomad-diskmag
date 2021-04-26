#
# Nomad Diskmag - BUTTONS
# Rendering buttons.
#
# E-zine on a 1.44 floppy tailored made on Raspberry Pi computer.
# Created by Krzysztof Krystian Jankowski
# https://krzysztofjankowski.com/nomad-diskmag
#

import sys
import pygame
from pygame.locals import *

class Button():
	font_directory = "assets"
	font_bold_filename = "CascadiaCode-Bold.ttf"
	font_size = 18

	def __init__(self, mag, text, pos, link, size=20, color="#f8f8f8", bg="#777777", shadow="#222222", pivot="center"):
		self.Mag = mag
		self.text = text
		self.pos = pos
		self.color = color
		self.bg = bg
		self.shadow = shadow
		self.shadow_shift  = (2,4)
		self.shift = (0,0)
		self.fontsize = size
		self.padding = 6
		self.link = link
		self.pivot = pivot
		font_path = "{base}/{sub}/{file}".format(base=getattr(sys, '_MEIPASS', '.'), sub=self.font_directory, file=self.font_bold_filename)
		self.font = pygame.font.Font(font_path, self.font_size)
		self.render()
		self.Mag.scene.buttons.append(self)
		self.Mag.scene.add(self)

	def render(self):
		self.rendered_text = self.font.render("  {text}  ".format(text=self.text), True, Color(self.color))
		self.rect = self.rendered_text.get_rect()
		if self.pivot == "left":
			self.rect.topleft = self.pos
		if self.pivot == "center":
			self.rect.midtop = self.pos

	def draw(self):
		pygame.draw.rect(self.Mag.screen, 
			Color(self.shadow), 
			(self.rect[0]+self.shadow_shift[0] - self.padding, 
			self.rect[1]+self.shadow_shift[1] - self.padding, 
			self.rect[2] + self.padding*2, 
			self.rect[3] + self.padding*2))
		pygame.draw.rect(self.Mag.screen, 
			Color(self.bg), 
			(self.rect[0]+self.shift[0] - self.padding,
			self.rect[1]+self.shift[1] - self.padding,
			self.rect[2] + self.padding*2,
			self.rect[3] + self.padding*2))
		self.Mag.screen.blit(self.rendered_text, (self.rect[0]+self.shift[0], self.rect[1]+self.shift[1], self.rect[2], self.rect[3]))
		
	def click(self, event):
		
		if event.type == MOUSEBUTTONDOWN:
			x, y = pygame.mouse.get_pos()
			if self.rect.collidepoint(x, y):
				self.shift = (2,2)
				return False

		if event.type == JOYBUTTONDOWN:
			x, y = self.Mag.cursor.get_pos()
			if self.rect.collidepoint(x, y):
				self.shift = (2,2)
				return False

		if event.type == MOUSEBUTTONUP:
			x, y = pygame.mouse.get_pos()
			if self.rect.collidepoint(x, y):
				return True
				
		if event.type == JOYBUTTONUP:
			x, y = self.Mag.cursor.get_pos()
			if self.rect.collidepoint(x, y):
				return True
		
		self.shift = (0,0)	
		return False
