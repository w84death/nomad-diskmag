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
CHAPTERS_DIR = "articles"

FDD_IMAGE = "assets/fdd.gif"
COVER_BG_COLOR = "#8a1630"
TITLE_BG_COLOR = "#62263f"
TEXT_COLOR = "#f8f8f8"

APP_WIDTH=480
APP_HEIGHT=640

## SETUP
Mag = App(title=APP_TITLE,
	width=APP_WIDTH,
	height=APP_HEIGHT)
ArticleBox = Box(Mag)
IndexBox = Box(Mag)
CoverBox = Box(Mag)

def SetupWindow():
	Mag.bg = COVER_BG_COLOR
	MenuBar(Mag,
		toplevel=["Index", "Magazine"],
		options=[
			[ 
				["Cover", ShowCover], 
				["Chapters", ShowIndex]
			],
			[
				["About", ShowAbout],
				["Close", CloseApp]
			]
		])

		
def CreateCover():
	Text(CoverBox, 
		text="Welcome to the",
		size=18,
		color=TEXT_COLOR,
		font="Liberation Sans")
	Text(CoverBox, 
		text="Raspberry Pi FDD Magazine",
		size=24,
		color=TEXT_COLOR,
		bg=TITLE_BG_COLOR,
		font="Liberation Sans")
	Text(CoverBox, 
		text="ISSUE #" + str(ISSUE),
		size=18,
		color=TEXT_COLOR,
		font="Liberation Sans")
	Picture(CoverBox,
		image=FDD_IMAGE)
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
	CoverBox.show()
	IndexBox.hide()
	ArticleBox.hide()
		
def CloseApp():
	Mag.destroy()

def ShowAbout():
	print("about")

def CreateIndex():
	Text(IndexBox, 
		text="CHAPTERS",
		size=24,
		color=TEXT_COLOR,
		font="Liberation Sans",
		width="fill")
	
	
	chapters = os.listdir(CHAPTERS_DIR)
	for chapter in chapters:
		title, author, article, line_cunt = GetChapterData(chapter)
		PushButton(IndexBox,
			command=ShowArticle,
			args=[chapter],
			text=title)

def ShowIndex():
	Mag.title = "{title} - CHAPTERS".format(title=APP_TITLE)
	IndexBox.show()
	CoverBox.hide()
	ArticleBox.hide()

def ShowArticle(chapter):
	title, author, article, line_cunt = GetChapterData(chapter)

	Mag.title = "{title} - {chapter}".format(title=APP_TITLE, chapter=title)
	Text(ArticleBox, 
		text=title,
		size=24,
		color=TEXT_COLOR,
		font="Liberation Sans",
		width="fill")
	Text(ArticleBox, 
		text="Writen by: {author} / Lines: {lines}".format(author=author, lines=line_cunt),
		size=12,
		color=TEXT_COLOR,
		font="Liberation Sans",
		width="fill")
	article_box = TextBox(ArticleBox, 
		text=article,
		enabled=False,
		multiline=True,
		scrollbar=True,
		align="left",
		width="fill",
		height="fill")
	article_box.text_size=14
	article_box.text_color=TEXT_COLOR
	article_box.font="Liberation Sans"
	ArticleBox.show()
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
	return title, author, article, line_count - 2

## RUN

SetupWindow()
CreateCover()
CreateIndex()
ShowCover()
Mag.display()