# file_lengths_counter with python

# 🗃️ File Analyzer & Logger in Python

This is a command-line Python application that lets users load and analyze multiple text files. It offers functionality such as counting characters, words, lines, finding occurrences of text, and logging actions to a file.

## 🔧 Features

- 📂 **Load multiple text files** into memory.
- 🔠 **Character count** (with or without spaces).
- 📏 **Line count**.
- 📝 **Word count**.
- 🔍 **Find text occurrences** (case-sensitive or insensitive).
- 📜 **View file contents**.
- 🧾 **Action log** — Keeps a record of all actions performed on files.
- 🗑️ **Delete log** when no longer needed.

## 📄 Sample Usage

```bash
$ python3 file_analyzer.py
```

You'll see a menu like:

```
=== File Context Menu ===
1. Load a new file
2. List loaded files
3. View character count
4. View line count
5. View word count
6. Find text occurrences
7. View log
8. Delete log file
9. View File
10. Exit
```

### ✅ Example Actions

- Load `file4.txt`
- View character count (with or without spaces)
- Count the number of lines or words
- Search how many times “python” appears in a file
- View and delete the `file_log.txt` which records all actions

## 📁 File Structure

```bash
.
├── main.py      # Main program
├── *file_log.txt          # Automatically generated log file
├── file1.txt             # Sample test file
├── file2.txt             # Sample test file
├── file3.txt             # Sample test file
├── file4.txt             # Sample test file
├── file5.txt             # Sample test file
└── README.md             # You're here
```

## 🧪 Test Files

This project comes with 5 test files that cover different use cases:
- Blank file
- Lines with extra spaces and tabs
- Mixed-case repeated words
- Multiline quote
- Simple short paragraph

You can easily add more `.txt` files for testing.

## 🧰 Requirements

- Python 3.x
- No external dependencies

## 📌 Notes

- Log file (`file_log.txt`) is created automatically after first action.
- If you try to load a non-existent file or one without read permission, you’ll get a clear error message.

---

Made with 💻 and 🧠 in Python