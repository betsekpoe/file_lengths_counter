from re import sub
import os

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
        return len(self.content.splitlines())

    def word_count(self):
         return len(self.content.split()) #splits everything seperated by a white space into its own element in an array

    def find_occurrences(self, text_to_find, case_sensitive = False):
        # counts occurrences directly if [case_sensitive] is True, else uses lowercase matching
        return self.content.count(text_to_find)  if case_sensitive else self.content.lower().count(text_to_find.lower())


def select_file(files, action="perform this action"):
    if not files:
        print("No files loaded!")
        return None
    print(f"Available files to {action}")
    for file in files:
        print(f"- {file}")
    filename = input("Enter a file: ")
    if filename in files:
        return filename
    print("File not found!")
    return None

file_log_name = "file_log.txt"

def post_to_log(filename, text_to_find, method = "", number = ""):
    with open(file_log_name, "a+") as log:
        if text_to_find and method and number:
                log.write(f"{filename}: {method} '{text_to_find}' - {number}\n")
        elif method and number:
            log.write(f"{filename}: {method} {number}\n")
        else:
            log.write(f"{filename} was created\n")


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
              "8. Delete log file\n"
              "9. View File\n"
              "10. Exit\n")
        menu_selection = input("Choose an option (1 - 10): ")
        print()

        if menu_selection == "1":
            print("Load file\n"
                  "Type 0 to return to context menu")
            filename = input("Enter a file name (eg: logs.txt): ")
            if filename == "0":
                continue
            file_obj = File(filename)
            if file_obj.success:
                files[filename] = file_obj
                print(f"File {filename} added successfully.\n")
                post_to_log(filename, "")
            else:
                print("File not added due to an error.\n")

        elif menu_selection == "2":
            if not files:
                print("No files loaded")
            else:
                print("Loaded files:")
                for file in files:
                    print(f"- {file}")

        elif menu_selection == "3":
            print("View character count")
            filename = select_file(files, "view character count")
            if filename:
                include_spaces = input("Include spaces in count? y/n: ").strip().lower() == "y"
                caption = "Characters including spaces:" if include_spaces == True else "Characters excluding spaces:"
                character_count = files[filename].character_count(include_spaces)
                print(caption, character_count)
                post_to_log(filename, "", method = "character_count", number = character_count,)

        elif menu_selection == "4":
            print("View line count")
            filename = select_file(files, "view line count")
            if filename:
                line_count = files[filename].line_count()
                print(f"{filename} has {line_count} lines")
                post_to_log(filename, "", method = "line count", number = line_count)

        elif menu_selection == "5":
            print("View word count")
            filename = select_file(files, "view word count")
            if filename:
                word_count = files[filename].word_count()
                print(f"{filename} has {word_count} words")
                post_to_log(filename, "", method = "word count", number = word_count)

        elif menu_selection == "6":
            print("Find text occurrences")
            filename = select_file(files, "find occurrences")
            if filename:
                text = input("Type in a word/text: ")
                case_sensitive = input("Find case sensitive matches y/n: ").strip().lower() == "y"
                occurrences = files[filename].find_occurrences(text, case_sensitive)
                print(f"{text} appeared {occurrences} times")
                post_to_log(filename, text_to_find = text, method = "found", number = occurrences)

        elif menu_selection == "7":
            try:
                print("File Log. File Actions")
                with open(file_log_name, "r") as file_log:
                    print(file_log.read())
            except FileNotFoundError:
                print("No logs yet!")

        elif menu_selection == "8":
            print("Are you sure you want to delete the log file?\nThis action cannot be undone!")
            confirm_delete = input("y/n: ") == "y"
            if confirm_delete and os.path.exists(file_log_name):
                try:
                    os.remove(file_log_name)
                    print(f"'{file_log_name}' deleted successfully!")
                except Exception as e:
                    print(f"Error deleting file {e}")
            else:
                print(f"{file_log_name} does not exist!")

        elif menu_selection == "9":
            filename = select_file(files, "view contents")
            if filename:
                print(f"Viewing content of {filename}")
                print(files[filename].content)

        elif menu_selection == "10":
            print("Exiting...")
            break

        else:
            print("Invalid selection! Choose options 1 - 10")

if __name__ == "__main__":
    file_menu()