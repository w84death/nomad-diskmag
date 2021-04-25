#
# Nomad Diskmag - Mag class
# Main loop and app initiation.
#
# E-zine on a 1.44 floppy tailored made on Raspberry Pi computer.
# Created by Krzysztof Krystian Jankowski
# https://krzysztofjankowski.com/nomad-diskmag
#

import pygame
from pygame.locals import *
from sources.chapter import Chapter
from sources.cursor import Cursor

class Mag:
	resolution = (0,0)
	flags = FULLSCREEN | HWSURFACE | DOUBLEBUF
	scenes = []
	current_scene = 0
	shortcuts = {
		K_1: 'self.change_scene(0)',
		K_2: 'self.change_scene(1)',
		K_n: 'self.next_scene()',
		K_m: 'self.change_page()',
		K_ESCAPE: 'self.quit()',
	}
	running = True
	drawing = False

	def __init__(self, resolution, caption, chapters):
		pygame.init()
		pygame.mouse.set_visible(False)
		pygame.display.set_caption(caption)
		
		Mag.resolution = resolution
		Mag.screen = pygame.display.set_mode(resolution) #, self.flags)
		Mag.chapter = Chapter(chapters)
		Mag.cursor = Cursor(self.screen, (100,50))
		Mag.clock = pygame.time.Clock()

		pygame.joystick.init()		
		if pygame.joystick.get_count() > 0:
			Mag.joystick = pygame.joystick.Joystick(0)
			Mag.joystick.init()

	def do_shortcut(self, event):
		k = event.key
		m = event.mod 
		
		if k in self.shortcuts:
			exec(self.shortcuts[k])

	def change_scene(self, scene_id):
		self.scene = self.scenes[scene_id]
		self.current_scene = scene_id
		self.scene.update()
		pygame.display.set_caption(self.scene.caption)  

	def change_page(self):
		self.scene.paginator.change_page()

	def next_scene(self):
		self.current_scene += 1
		if self.current_scene > len(self.scenes) - 1:
				self.current_scene = 0
		self.change_scene(self.current_scene)

	def go_next_virtual_page(self):
		if not self.scene.paginator.change_page():
			self.next_scene()

	def quit(self):
		self.running = False

	def start_drawing(self):
		self.drawing = True
		
	def loop(self):
		while self.running:
			if pygame.joystick.get_count() > 0:
				self.cursor.move(self.joystick.get_axis(0), self.joystick.get_axis(1))

			for event in pygame.event.get():
				if event.type == QUIT:
					self.running = False
				if event.type == KEYDOWN:
					self.do_shortcut(event) 	
				
				self.cursor.update(event)

				for button in self.scene.buttons:
					if button.click(event):
						exec(button.link)
						
			if self.drawing:
				self.scene.draw()
			self.clock.tick(24)

		pygame.quit()

if __name__ == '__main__':
	Mag(resolution=(480,640), caption="Main").loop()
