import os
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
        with open("{dir}/{filename}".format(dir=self.directory, filename=chapter_filename),
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