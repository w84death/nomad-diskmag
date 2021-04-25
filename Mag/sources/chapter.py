#
# Nomad Diskmag - CHAPTERS
# Chapter represent one article in a text file (in /chapters/).
#
# E-zine on a 1.44 floppy tailored made on Raspberry Pi computer.
# Created by Krzysztof Krystian Jankowski
# https://krzysztofjankowski.com/nomad-diskmag
#

import sys
class Chapter:
	directory = "chapters"
	collection = []

	def __init__(self, chapters):
		self.chapters = chapters
		self.get_collection()

	def get_collection(self):
		for chapter_filename in self.chapters:
			title, author, article = self.get_data(chapter_filename)
			self.collection.append((chapter_filename, title, author, article))

	def get_data(self, chapter_filename):
		line_count = 0
		article = ""
		chapter_path = "{base}/{sub}/{file}".format(base=getattr(sys, '_MEIPASS', '.'), sub=self.directory, file=chapter_filename)
		with open(chapter_path,encoding="utf8", mode="r") as file:
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