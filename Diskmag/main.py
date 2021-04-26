#
# Nomad Diskmag - MAIN FILE
# Current issue configuration with page layouts.
#
# E-zine on a 1.44 floppy tailored made on Raspberry Pi computer.
# Created by Krzysztof Krystian Jankowski
# https://krzysztofjankowski.com/nomad-diskmag
#

from sources.mag import Mag
from sources.chapter import Chapter
from sources.text import Text
from sources.scene import Scene
from sources.clipart import Clipart
from sources.button import Button

import math

class MagazineIssue0(Mag):
	engine_version = "0.999"
	resolution = (1280, 720)
	caption = "Nomad Diskmag"
	chapters = ("intro.txt", "why-pi.txt", "python-fun.txt", "test.txt")

	def __init__(self):
		super().__init__(resolution=self.resolution, caption=self.caption, chapters=self.chapters)
		hw, hh  = (self.resolution[0]*0.5, self.resolution[1]*0.5)
		bottom = self.resolution[1] - 40
		left = 70
		right = self.resolution[0] - 70

		# COVER
		Scene(Mag, Text, caption='Cover', notitle=True, bg="#ccc39d", color="white", cursor=["#222222","#ee4444", "#ffeecc"])
		Clipart(Mag, "rainbow", (0,0))
	
		logo_tail = 42
		step = 16
		for nd in range(logo_tail):
			c = "#fafafa"
			if (nd == logo_tail-1):
				c = "#222222"
			temp_x = right + 96 - nd * step
			Text(Mag, "./N0MAD", pos=(temp_x, bottom-nd*step), size=128, color=c, align="center", bold=True)
			Text(Mag, "DISKMAG", pos=(temp_x, bottom+100-nd*step), size=128, color=c, align="center", bold=True)
		

		Clipart(Mag, "cover_0", (hw-152/2,500), transparent="#ccc39d")
		
		Text(Mag, "Issue #0", pos=(left,bottom-96), size=48, color="#ffffff")
		Text(Mag, "04/2021", pos=(left,bottom-32), size=48, color="#ffffff")

		Text(Mag, "Engine Version: [{v}]".format(v=self.engine_version), pos=(hw,bottom), size=14, align="center", color="#ffffff")
		Button(Mag, "Run Diskmag!", (hw, hh), "self.go_next_virtual_page()")

		# CHAPTERS / INDEX
		Scene(Mag, Text, caption='Chapters', title="Chapters", bg="#eeeeee", align="center", cursor=["#000000","#444499","#9999ff"])
		Text(Mag, 'Index of the issue', pos=(hw,70), align="center")
		Clipart(Mag, "floppy", (hw-152/2,bottom-70), transparent="#eeeeee", palette=("#1c6cb2", "#3294e5", "#b7cfe5"))
		Button(Mag, "Cover", (left,bottom), "self.change_scene(0)", pivot="left")
		Button(Mag, "Start reading", (right,bottom), "self.go_next_virtual_page()", pivot="right")

		index = 2
		for chapter in Mag.chapter.collection:
			Button(Mag, chapter[1], (hw*0.5, 45 + (50*index)), "self.change_scene({scene})".format(scene=index), pivot="left")
			index += 1

		Button(Mag, "Close Diskmag", (hw, bottom-128), "self.quit()")

		# INDIVIDUAL CHAPTERS
		for chapter in Mag.chapter.collection:
			filename, title, author, article = chapter
			Scene(Mag, Text, caption=title, title=title)
			Text(Mag, author, pos=(70,60), color="#777777")
			pages = Text(Mag, article, pos=(70,100)).pages
			Clipart(Mag, "floppy", (hw+152+76,hh), transparent="#eeeeee",)
			if pages > 0:
				Button(Mag, "Change page..", (hw,bottom), "self.change_page()", pivot="center")
			Button(Mag, "Next chapter", (right,bottom), "self.next_scene()", pivot="right")
			Button(Mag, "Chapters", (left, bottom), "self.change_scene(1)", pivot="left")

		# OUTRO
		Scene(Mag, Text, caption="Outro", title="Thanks for reading", bg="black", color="white", align="center")
		Text(Mag, "Do you want to be included in the next issue? Contact me at kj@p1x.in with your article.", pos=(hw,70), align="center", color="white", column_limit=50)
		Text(Mag, "You can support me at https://liberapay.com/cyfrowynomada/.", pos=(hw, 130), color="#f6c915", align="center", column_limit=50)
		Clipart(Mag, "floppy", (hw-152/2,hh), transparent="black", palette=("#727272", "#939293", "#c6c6c6"))

		Button(Mag, "Rewind", (hw, bottom-64), "self.change_scene(0)")
		Button(Mag, "Close Diskmag", (hw, bottom), "self.quit()")

		# START FROM 0
		self.change_scene(0)
		self.start_drawing()

if __name__ == '__main__':
	MagazineIssue0().loop()
