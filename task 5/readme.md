# 🧾 Student Marks Dictionary Program

## 📘 Problem Statement
Write a Python program that:
1. Creates a dictionary where student names are keys and their marks are values.  
2. Asks the user to input a student's name.  
3. Retrieves and displays the corresponding marks.  
4. If the student’s name is not found, display an appropriate message and optionally allow adding a new student.  




## 🧠 Program Logic

 A dictionary named `students` stores predefined student names and their marks.  
   students = {"sahil": 100, "alice": 95, "rohan": 85}
The user is prompted to enter a student’s name.

The program checks:

If the name exists in the dictionary → display the student’s marks.

If not → show a message "student not found".

The user can choose to add a new student:

If yes, input marks (validated between 0 and 100).

If no, display a thank-you message.

The dictionary updates dynamically when a new student is added.
