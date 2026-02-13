"""
Problem Statement: Write a Python program that:
1.   Takes user input and writes it to a file named output.txt.
2.   Appends additional data to the same file.
3.   Reads and displays the final content of the file.
"""
text_to_write=input("enter the text to write to file:")
try:
    #user input into output.txt
    with open("output.txt","wt") as fh:
        fh.write(text_to_write+"\n")
    print("data succesfully written to output.txt.")
    #appened data into the file
    text_to_Appened=input("enter additional text to add")
    with open("output.txt","at") as fh:
        fh.write(text_to_Appened+"\n")
        print("data succesfully added\n")
    #read the final file 
    print("the final details are as ")
    with open("output.txt","rt") as fh:
            print(fh.read())
        
except Exception as err:
    print(f"AN ERROR ERROR OCCURED  {err} TRY AGAIN ")