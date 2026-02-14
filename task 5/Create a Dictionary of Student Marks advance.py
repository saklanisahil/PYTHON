"""Problem Statement: Write a Python program that:
1.   Creates a dictionary where student names are keys and their marks are values.
2.   Asks the user to input a student's name.
3.   Retrieves and displays the corresponding marks.
4.   If the student’s name is not found, display an appropriate message.
"""
#adding data to dictonaries
student={}
choice=int(input("enter the number of students"))
for i in range(choice):
    name=input("enter the student name ")
    marks=int(input ("enter student maarks out of 100 "))
    if 0<=marks<=100:
        student[name]=marks
    else:
        print("marks cannot be greater than 100 or less than 0 please enter vaild marks")

print(student)


check=input("enter the name to find ")
if check==name:
    print(f"{name} has got marks:{student[marks]}")
else:
    print("student not found please recheck and try again")