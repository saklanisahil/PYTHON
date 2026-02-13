TASK 1 
# File Handling in Python

## 🧾 Task Description
This Python program demonstrates **basic file handling** operations such as:
1. Opening and reading a text file named `Sample.text`
2. Printing its contents line by line
3. Handling errors gracefully if the file does not exist

---

## 🛠️ How It Works
- The program first attempts to open and read `Sample.text`.
- If the file exists, it prints each line neatly using `strip()` to remove extra spaces and newlines.
- If the file is **not found**, it catches the `FileNotFoundError` and displays a helpful message.

There’s also a commented-out section that can **create the file** automatically if it doesn’t exist.

---




TASK 2 
# Write, Append, and Read Data from a File in Python

## 🧾 Problem Statement
Write a Python program that:
1. Takes user input and writes it to a file named `output.txt`.
2. Appends additional data to the same file.
3. Reads and displays the final content of the file.

---

## 🛠️ How It Works
1. The program first asks the user for some text and **writes** it to `output.txt` using **write mode (`"wt"`)**.
2. It then asks for additional text and **appends** it to the same file using **append mode (`"at"`)**.
3. Finally, it **reads** and prints the complete content of the file using **read mode (`"rt"`)**.
4. All file operations are wrapped in a `try-except` block to handle errors gracefully.

---

## 💻 Code Example

```python
"""
Problem Statement: Write a Python program that:
1.   Takes user input and writes it to a file named output.txt.
2.   Appends additional data to the same file.
3.   Reads and displays the final content of the file.
"""

text_to_write = input("Enter the text to write to file: ")

try:
    # Write user input into output.txt
    with open("output.txt", "wt") as fh:
        fh.write(text_to_write + "\n")
    print("Data successfully written to output.txt.")

    # Append additional data into the file
    text_to_append = input("Enter additional text to add: ")
    with open("output.txt", "at") as fh:
        fh.write(text_to_append + "\n")
    print("Data successfully added.\n")

    # Read and display the final file content
    print("The final details are as follows:")
    with open("output.txt", "rt") as fh:
        print(fh.read())

except Exception as err:
    print(f"An error occurred: {err}. Try again.")

