#
# Raspberry Pi FDD Magazine - Issue #1
# 
# Magazine on a 1.44 floppy tailored for Raspberry Pi computers. 
# Created by Krzysztof Krystian Jankowski
# https://krzysztofjankowski.com/pifddmag
#

from mag import *

class MagazineIssue1(Mag):
    def __init__(self):
        super().__init__(resolution=(480,640), caption="Raspberry Pi FDD Magazine")
        
        Scene(caption='Cover', title="Raspberry Pi FDD Magazine - Issue #1", bg="red", align="center")
        Text('Welcome to the magazine!', pos=(240,25), align="center")
        Picture(file="fdd.gif", pos=(240,320))

        Scene(caption='Chapters', title="Chapters", bg="yellow")
        Text('Index of the issue', pos=(0,25))
        index = 2
        for chapter in Mag.chapter.collection:
            Text(chapter[0], pos=(0,25*index))
            index += 1

        Scene(caption='Chapters', title="Chapter 1 - Introduction")
        chapter_data = Mag.chapter.get_data("1.txt")
        Text(chapter_data[1], pos=(0,50))
        Text(chapter_data[2], pos=(0,75))
        Picture(file="raspi.gif", pos=(240,320))
        

        self.change_scene(0)
        self.start_drawing()
        
if __name__ == '__main__':
    MagazineIssue1().loop()