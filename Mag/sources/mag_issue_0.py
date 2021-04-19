#
# Raspberry Pi FDD Magazine - Issue #1
# 
# Magazine on a 1.44 floppy tailored for Raspberry Pi computers. 
# Created by Krzysztof Krystian Jankowski
# https://krzysztofjankowski.com/pifddmag
#

from mag import *

class MagazineIssue1(Mag):
	resolution = (640,480)
	
	half = (resolution[0]*0.5, resolution[1]*0.5)
	caption = "Raspberry Pi FDD Diskmag"
	chapters = ("intro.txt", "why-pi.txt", "python-fun.txt", "test.txt")

	def __init__(self):
		super().__init__(resolution=self.resolution, caption=self.caption, chapters=self.chapters)
		hw = self.half[0]
		hh = self.half[1]
		bottom = self.resolution[1] - 34
		left = 60
		right = self.resolution[0] - 84

		# COVER
		Scene(Mag, Text, caption='Cover', notitle=True, bg="#ccc39d", color="white")
		Text(Mag, "by Krzysztof Krystian Jankowski", pos=(hw,260), size=14, align="center", color="#888888")
		
		Clipart(Mag, "cover_0", (hw-152/2,250), transparent="#ccc39d")
		Text(Mag, "RASPBERRY", pos=(hw,55), size=36, color="#222222", align="center", bold=True)
		Text(Mag, "DISKMAG", pos=(hw,90), size=36, color="#222222", align="center", bold=True)

		Text(Mag, "Issue #0, 04/2021", pos=(hw,150), align="center", size=28, color="#b21cb0")

		Button(Mag, "Start reading!", (hw,bottom), "self.go_next_virtual_page()")

		# CHAPTERS / INDEX
		Scene(Mag, Text, caption='Chapters', title="Chapters", bg="#eeeeee", align="center")
		Text(Mag, 'Index of the issue', pos=(hw,45), align="center")
		Clipart(Mag, "floppy", (hw-152/2,bottom-70), transparent="#eeeeee", palette=("#1c6cb2", "#3294e5", "#b7cfe5"))
		Button(Mag, "< Cover", (left,bottom), "self.change_scene(0)")
		Button(Mag, "Next page >>", (right,bottom), "self.go_next_virtual_page()")	
		
		index = 2
		for chapter in Mag.chapter.collection:
			Button(Mag, chapter[1], (hw*0.5, 45 + (30*index)), "self.change_scene({scene})".format(scene=index), pivot="left")
			index += 1

		# INDIVIDUAL CHAPTERS
		for chapter in Mag.chapter.collection:
			filename, title, author, article = chapter
			Scene(Mag, Text, caption=title, title=title)
			Text(Mag, author, pos=(12,45), color="#777777")
			Text(Mag, article, pos=(12,75))
			Button(Mag, "Next page >>", (right,bottom), "self.go_next_virtual_page()")
			Button(Mag, "Index", (hw, bottom), "self.change_scene(1)")

		# OUTRO
		Scene(Mag, Text, caption="Outro", title="Thanks for reading", bg="black", color="white", align="center")
		Text(Mag, "Do you want to be included in the next issue? Contact me at kj@p1x.in with your article.", pos=(hw,60), align="center", color="white", column_limit=50)
		Clipart(Mag, "floppy", (hw-152/2,hh), transparent="black", palette=("#727272", "#939293", "#c6c6c6"))

		# START FROM 0
		self.change_scene(0)
		self.start_drawing()
		
if __name__ == '__main__':
	MagazineIssue1().loop()
