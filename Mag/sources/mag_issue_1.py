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
        
        page_cover = Scene(caption='Cover', title="Raspberry Pi FDD Magazine - Issue #1", bg="red")
        Text('Welcome to the magazine!', pos=(0,25))
        Text('Welcome to the magazine!', pos=(0,25))
        Picture(file="fdd.gif", pos=(240,320))

        page_chapters = Scene(caption='Chapters', title="Chapters")
        Text('Index of the issue', pos=(0,25))

        self.change_scene(0)
        self.start_drawing()
        
if __name__ == '__main__':
    MagazineIssue1().loop()