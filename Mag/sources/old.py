#
# Raspberry Pi FDD Magazine
# 
# Magazine on a 1.44 floppy tailored for Raspberry Pi computers. 
# Created by Krzysztof Krystian Jankowski
# https://krzysztofjankowski.com/pifddmag
#

import os
from guizero import App, MenuBar, Text, Picture, PushButton, TextBox, Window, Box

## CONFIG
APP_TITLE = "RPiFDDMag #1"
ISSUE = 1

APP_VERSION = "0.01"
APP_WIDTH = 480
APP_HEIGHT = 640
CHAPTERS_DIR = "chapters"
COVER_IMAGE = "assets/fdd.gif"
COVER_BG_COLOR = "#8a1630"
MAG_BG_COLOR = "#351a06"
ART_BG_COLOR = "#1b1b1b"
TEXT_COLOR = "#f8f8f8"
TITLE_BG_COLOR = "#62263f"


## SETUP
Mag = App(title=APP_TITLE,
	width=APP_WIDTH,
	height=APP_HEIGHT)
ChapterBox = Box(Mag, width="fill", height="fill")
IndexBox = Box(Mag)
CoverBox = Box(Mag)

article_title = Text(ChapterBox, 
	text="",
	size=24,
	width="fill")
article_info = Text(ChapterBox, 
	text="",
	size=11,
	width="fill")
article_body = TextBox(ChapterBox, 
	text="",
	enabled=False,
	multiline=True,
	scrollbar=True,
	align="left",
	width="fill",
	height="fill")

def SetupWindow():
	Mag.bg = COVER_BG_COLOR
	Mag.font = "Liberation Sans"
	Mag.text_size = 14
	Mag.text_color =  TEXT_COLOR
	
	MenuBar(Mag,
		toplevel=["Magazine", "About"],
		options=[
			[ 
				["List Chapters", ShowIndex],
				["Show Cover", ShowCover],
				["Close", CloseApp]
			],
			[
				["Application", ShowAbout],
			]
		])

		
def CreateCover():
	Text(CoverBox, 
		text="Welcome to the",
		size=18)
	Text(CoverBox, 
		text="Raspberry Pi FDD Magazine",
		size=24)
	Text(CoverBox, 
		text="ISSUE #" + str(ISSUE),
		size=18)
	Picture(CoverBox,
		image=COVER_IMAGE)
	BottomMenu = Box(CoverBox, 
		align="bottom",
		width=int(APP_WIDTH*0.75),
		height=48)
	PushButton(BottomMenu,
		command=ShowIndex,
		text="Start reading",
		align="left")
	PushButton(BottomMenu,
		command=CloseApp,
		text="Close magazine",
		align="right")

def ShowCover():
	Mag.title = "{title} - COVER".format(title=APP_TITLE)
	Mag.bg = COVER_BG_COLOR
	CoverBox.show()
	IndexBox.hide()
	ChapterBox.hide()
		
def CloseApp():
	Mag.destroy()

def ShowAbout():
	Mag.info("About", "RPi FDD Mag\nVersion {version}\ngithub.com/w84death/rpi-fdd-mag".format(version=APP_VERSION))

def CreateIndex():
	Text(IndexBox, 
		text="CHAPTERS",
		size=24,
		width="fill")
	
	
	chapters = os.listdir(CHAPTERS_DIR)
	for chapter in chapters:
		title, author, article = GetChapterData(chapter)
		PushButton(IndexBox,
			command=ShowArticle,
			args=[chapter],
			text=title)

def ShowIndex():
	Mag.bg = MAG_BG_COLOR
	Mag.title = "{title} - CHAPTERS".format(title=APP_TITLE)
	IndexBox.show()
	CoverBox.hide()
	ChapterBox.hide()

def ShowArticle(chapter):
	Mag.bg = ART_BG_COLOR
	title, author, article = GetChapterData(chapter)

	Mag.title = "{title} - {chapter}".format(title=APP_TITLE, chapter=title)
	article_title.value = title
	article_info.value = "Writen by {author}".format(author=author)
	article_body.value = article 
	ChapterBox.show()
	IndexBox.hide()

def GetChapterData(chapter):
	line_count = 0
	article = ""
	with open("{dir}/{filename}".format(dir=CHAPTERS_DIR, filename=chapter),
		encoding="utf8", 
		mode="r") as file:
		for line in file:
			if line_count == 0:
				title = line.rstrip()
			if line_count == 1:
				author = line.rstrip()
			if line_count >= 2:
				article += line
			line_count += 1
	
	file.close()
	return title, author, article

## RUN

SetupWindow()
CreateCover()
CreateIndex()
ShowCover()
Mag.display()