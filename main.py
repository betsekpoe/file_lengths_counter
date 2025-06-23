from re import sub

class File:
    def __init__(self, filename):
        self.file = open(filename, "r")
        self.content = self.file.read()

    def character_count(self, spaces = ""):
        count = None
        if spaces == "s".lower():
            count =  len(self.content)
        elif spaces == "":
            count = len(sub(r"\s+", "", self.content))
        return count

    def line_count(self):
        #line_count = 0
        #for c in text:
        #    if c == "\n":
        #        line_count += 1
        #line_count += 1"""
        pass

    def word_count(self):
        pass

    def find_occurrences(self, word_to_find):
        #print(f.count(word_to_find, 0))
        pass

file1 = File("dummy_text.txt")
print(f"Character count (with spaces): {file1.character_count('s')}")
