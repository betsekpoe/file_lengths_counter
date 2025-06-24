from re import sub

class File:
    def __init__(self, file):
        self.file = file
        # opens a file and reads into [content]
        try:
            with open(file, "r") as file:
                self.content = file.read()
        except FileNotFoundError: # if file is not found
            print(f"File or path {file} not found!")
            self.content = ""
        except PermissionError: # if permission is denied
            print(f"You do not have permission to add this file")
            self.content = ""

    def character_count(self, include_spaces = False):
        # returns the length of a string, or replaces recurring white spaces with nothing if [include_spaces] is  False
        return len(self.content) if include_spaces else len(sub(r"\s+", "", self.content))

    def line_count(self):
        line_count = 0
        for character in self.content:
           if character == "\n":
               line_count += 1
        line_count += 1
        return line_count

    def word_count(self):
         return len(self.content.split()) #splits everything seperated by a white space into its own element in an array

    def find_occurrences(self, text_to_find, case_sensitive = False):
        # converts text to lowercase and counts its lowercase occurrences if [case_sensitive] if True, or counts occurrences directly if [case_sensitive] is False
        return self.content.lower().count(text_to_find.lower()) if case_sensitive else self.content.count(text_to_find)


def file_menu():
    pass

# TODO:
# open multiple files and work on them
# (Count words, characters, lines, occurrences etc)
#
# - Anytime a count is made, it is stored in a file name "counter_logs" in the format:
#     filename characters ------------- x
#     filename lines ------------------ y
#     filename words ------------------ z
#     filename "abc" occurrences ------ w
#
# === File Context Menu ===
# 1. Load a new file
# 2. List loaded files
# 3. View character count
# 4. View line count
# 5. View word count
# 6. Find text occurrences
# 7. View log
# 8. Exit

if __name__ == "__main__":
    file_menu()