"""Problem Statement: Write a Python program that:
1.   Creates a dictionary where student names are keys and their marks are values.
2.   Asks the user to input a student's name.
3.   Retrieves and displays the corresponding marks.
4.   If the student’s name is not found, display an appropriate message.
"""
#dictonary created
students={"sahil":100,
          "alice":95,
          "rohan":85}


#user input
check_name=input("enter student name")
if check_name in students:
    print (f"{check_name} marks:{students[check_name]}")
else:
    print("student not found")
    choice=input("want to add student(yes/no)".lower())
    if choice=="yes":
        marks=int(input("enter the markds of the student(0-100) "))
        if 0<=marks<=100:
            students[check_name]=marks
        else:
            print("marks cannot be greater than 100 or less than 0 please enter vaild marks")
        print(students)
        print("details add successfully" )
    elif choice=="no":
        print("ok thank you")
    else:
        print ("enter a valid choice")

        