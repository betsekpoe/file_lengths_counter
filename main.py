from re import sub

class File:
    def __init__(self, file):
        self.file = file
        self.success = False

        # opens a file and reads into [content]
        try:
            with open(file, "r") as file:
                self.content = file.read()
                self.success = True
        except FileNotFoundError: # if file is not found
            print(f"File {file} not found!")
            self.content = ""
        except PermissionError: # if permission is denied
            print(f"You do not have permission to add this file.")
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
        # converts text to lowercase and counts its lowercase occurrences if [case_sensitive] is True, or counts occurrences directly if [case_sensitive] is False
        return self.content.lower().count(text_to_find.lower()) if case_sensitive else self.content.count(text_to_find)


def file_menu():
    files = {}

    while True:
        print("\n=== File Context Menu ===\n"
              "1. Load a new file\n"
              "2. List loaded files\n"
              "3. View character count\n"
              "4. View line count\n"
              "5. View word count\n"
              "6. Find text occurrences\n"
              "7. View log\n"
              "8. Exit")
        menu_selection = input("Choose an option (1 - 8): ")

        while menu_selection == "1":
            print("\nLoad file\n"
                  "Type 0 to return to context menu")
            filename = input("Enter a file name (eg: logs.txt): ")

            if File(filename).success:
                files[filename] = File(filename)
                print(files)
                print(f"File {filename} added successfully.")
            elif filename == "0":
                menu_selection = "0"
            else:
                print("File not added due to an error.\n")

        if menu_selection == "2":
            print("\nLoaded Files:")
            if not files:
                print("No files loaded")
            else:
                print("Loaded files:")
                for file in files:
                    print(f"- {file}")

        elif menu_selection == "3":
            print("View character count")
            if not files:
                print("No files loaded!")
            else:
                print("Available files:")
                for file in files:
                    print(f"{file}")

            filename = input("Enter a file: ")
            if filename in files:
                include_spaces = input("Include spaces in count? y/n: ") == "y".lower()
                caption = "Characters including spaces:" if include_spaces == True else "Characters excluding spaces:"
                print(caption, files[filename].character_count())
            else:
                print("File not found!")


        elif menu_selection == "8":
            print("Exiting...")
            break

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