import pygame
from pygame.locals import *

class Button():
	fontname = pygame.font.match_font("Liberation Sans")

	def __init__(self, mag, text, pos, link, size=20, color="#f8f8f8", bg="#444444"):
		self.Mag = mag
		self.text = text
		self.pos = pos
		self.color = color
		self.bg = bg
		self.fontsize = size
		self.link = link
		self.render()
		self.Mag.scene.buttons.append(self)
		self.Mag.scene.add(self)

	def render(self):
		font = pygame.font.Font(self.fontname, self.fontsize)
		self.rendered_text = font.render("  {text}  ".format(text=self.text), True, Color(self.color))
		self.rect = self.rendered_text.get_rect()
		self.rect.center = self.pos

	def draw(self):
		pygame.draw.rect(self.Mag.screen, Color(self.bg), self.rect)
		self.Mag.screen.blit(self.rendered_text,self.rect)
		
	def click(self, event):
		x, y = pygame.mouse.get_pos()
		if event.type == pygame.MOUSEBUTTONDOWN:
			if pygame.mouse.get_pressed()[0]:
				if self.rect.collidepoint(x, y):
					return True
		return False
