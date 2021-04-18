#
# Raspberry Pi FDD Magazine - Issue #1
# 
# Magazine on a 1.44 floppy tailored for Raspberry Pi computers. 
# Created by Krzysztof Krystian Jankowski
# https://krzysztofjankowski.com/pifddmag
#

from mag import *

class MagazineIssue1(Mag):
    resolution = (480,645)
    caption = "Raspberry Pi FDD Diskmag"
    chapters = ("intro.txt", "why-pi.txt", "test.txt")

    def __init__(self):
        super().__init__(resolution=self.resolution, caption=self.caption, chapters=self.chapters)
        
        # COVER
        Scene(Mag, Text, caption='Cover', title="Raspberry Pi FDD Diskmag", bg="red", color="white", align="center")
        Text(Mag, 'Issue #0.999', pos=(245,45), align="center", size=28, color="white")
        Text(Mag, 'Welcome to the magazine! Fresh from the floppy..', pos=(245,90), align="center", color="white")
        Picture(Mag, file="fdd.gif", pos=(245,320))

        # CHAPTERS / INDEX
        Scene(Mag, Text, caption='Chapters', title="Chapters", bg="yellow")
        Text(Mag, 'Index of the issue', pos=(0,45))
        index = 2
        for chapter in Mag.chapter.collection:
            Text(Mag, chapter[1], pos=(0,45 + (25*index)))
            index += 1

        # INDIVIDUAL CHAPTERS
        for chapter in Mag.chapter.collection:
            filename, title, author, article = chapter
            Scene(Mag, Text, caption=title, title=title)
            Text(Mag, author, pos=(0,45))
            Text(Mag, article, pos=(0,75))

        # OUTRO
        Scene(Mag, Text, caption="Outro", title="Thanks for reading", bg="black", color="white", align="center")
        Text(Mag, "Do you want to be included in the next issue? Contact me at kj@p1x.in with your article.", pos=(245,45), align="center", color="white")

        # START FROM 0
        self.change_scene(0)
        self.start_drawing()
        
if __name__ == '__main__':
    MagazineIssue1().loop()