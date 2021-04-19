import pygame
from pygame.locals import *

class Button():
	fontname = pygame.font.match_font("Liberation Sans")

	def __init__(self, mag, text, pos, link, size=20, color="#f8f8f8", bg="#777777", shadow="#222222", pivot="center"):
		self.Mag = mag
		self.text = text
		self.pos = pos
		self.color = color
		self.bg = bg
		self.shadow = shadow
		self.shadow_shift  = (2,2)
		self.shift = (0,0)
		self.fontsize = size
		self.link = link
		self.pivot = pivot
		self.render()
		self.Mag.scene.buttons.append(self)
		self.Mag.scene.add(self)

	def render(self):
		font = pygame.font.Font(self.fontname, self.fontsize)
		self.rendered_text = font.render("  {text}  ".format(text=self.text), True, Color(self.color))
		self.rect = self.rendered_text.get_rect()
		if self.pivot == "left":
			self.rect.topleft = self.pos
		if self.pivot == "center":
			self.rect.midtop = self.pos

	def draw(self):
		pygame.draw.rect(self.Mag.screen, Color(self.shadow), (self.rect[0]+self.shadow_shift[0], self.rect[1]+self.shadow_shift[1], self.rect[2], self.rect[3]))
		pygame.draw.rect(self.Mag.screen, Color(self.bg), (self.rect[0]+self.shift[0], self.rect[1]+self.shift[1], self.rect[2], self.rect[3]))
		self.Mag.screen.blit(self.rendered_text, (self.rect[0]+self.shift[0], self.rect[1]+self.shift[1], self.rect[2], self.rect[3]))
		
	def click(self, event):
		x, y = pygame.mouse.get_pos()
		if event.type == pygame.MOUSEBUTTONDOWN:
			if pygame.mouse.get_pressed()[0]:
				if self.rect.collidepoint(x, y):
					self.shift = (2,2)
					return False

		if event.type == pygame.MOUSEBUTTONUP:
			if self.rect.collidepoint(x, y):
				return True
		self.shift = (0,0)	
		return False
