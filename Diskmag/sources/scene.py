#
# Nomad Diskmag - SCREENS
# Managing screens. Renders window title and first header on each screen.
#
# E-zine on a 1.44 floppy tailored made on Raspberry Pi computer.
# Created by Krzysztof Krystian Jankowski
# https://krzysztofjankowski.com/nomad-diskmag
#

import pygame
from pygame.locals import *

class Scene:
	id = 0
	bg = Color('white')

	def __init__(self, mag, text, caption="Window Caption", title="Scene Title", notitle=False, bg="white", color="black", align="left", cursor=["#222222","#ffaacc","#eeeeee"], track=""):
		self.Mag = mag
		self.Text = text
		self.Mag.scenes.append(self)
		self.Mag.scene = self
		self.id = Scene.id
		Scene.id += 1
		self.nodes = []
		self.buttons = []
		self.bg = Color(bg)
		self.cursor_palette = cursor
		self.caption = caption
		self.track = track
		if notitle == False:
			aligned_pos = (12,32)
			if align == "center":
				aligned_pos = (self.Mag.resolution[0] * 0.5, 32)
			self.add(self.Text(self.Mag, title, size=32, pos=aligned_pos, align=align, bold=True, color=color, column_limit=90))

	def ready(self):
		self.Mag.cursor.update_palette(self.cursor_palette)
		if self.track != "":
			self.Mag.midi.play_track(self.track)

	def draw(self):
		self.Mag.screen.fill(self.bg)
		for node in self.nodes:
			node.draw()
		self.Mag.cursor.draw()
		pygame.display.flip()

	def add(self, element):
		self.nodes.append(element)

	def __str__(self):
		return 'Scene {}'.format(self.id)

	