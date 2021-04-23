#
# Nomad Diskmag - TEXTS
# Rendering block of text, split in pages.
#
# E-zine on a 1.44 floppy tailored made on Raspberry Pi computer.
# Created by Krzysztof Krystian Jankowski
# https://krzysztofjankowski.com/nomad-diskmag
#

import pygame
from pygame.locals import *
from itertools import chain
import textwrap

class Text():
	fontname = "assets/CascadiaCode-Light.ttf"
	fontboldname = "assets/CascadiaCode-Bold.ttf"
	fontsize = 18
	line_height = 18
	fontcolor = Color('black')
	page = 0
	max_lines = 30
	column_limit = 55

	def __init__(self, mag, text, pos, size=18, color="black", align="left", bold=False, column_limit=55, page=0):
		self.Mag = mag
		self.text = text
		self.page = page
		self.pos = pos
		self.align = align
		self.fontsize = size
		self.fontcolor = Color(color)
		self.column_limit = column_limit
		self.rendered_data = []
		if bold:
			self.font = pygame.font.Font(self.fontboldname, self.fontsize)
		else:
			self.font = pygame.font.Font(self.fontname, self.fontsize)
		self.render()
		self.Mag.scene.add(self)
		self.Mag.scene.paginator = self

	def render(self):
		line = 0
		page = 0
		wrapped_text = []

		for paragraph in self.text.split('\n'):
			wrapped_text.append(textwrap.fill(paragraph, self.column_limit))


		for part in wrapped_text:
			for line_of_text in part.split('\n'):
				rendered_text = self.font.render(line_of_text, True, self.fontcolor)
				rect = rendered_text.get_rect()

				if self.align == "left":
					rect.topleft = self.pos
				if self.align == "center":
					rect.midtop = self.pos

				rect[1] += self.line_height * line
				self.rendered_data.append((rendered_text, rect, page))
				if(line >= self.max_lines):
					page += 1
					line = 0
				line += 1

		self.pages = page


	def change_page(self):
		self.page += 1
		if self.page > self.pages:
			self.page = 0
			return False
		return True

	def draw(self):
		for data in self.rendered_data:
			if data[2] == self.page:
				self.Mag.screen.blit(data[0],data[1])
