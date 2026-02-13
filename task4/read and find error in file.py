
"""1.   Opens and reads a text file named sample.txt.
2.   Prints its content line by line.
3.   Handles errors gracefully if the file does not exist."""

        #creating a file named sample and adding text to it
'''with open("Sample.text","xt") as fh:
    fh.write("hi this is sahil\n hope you doing good it was nice to meet you ")
    print("file created succesfully")'''
    
try:                                        
    with open("Sample.text","rt") as fh:
#for large files 
        for line in fh:  # Reads line by line lazily
            print(line.strip())
#for small files 
        """line =fh.readlines()
        print((line))   #reads the data as a whole in list
        print(("".join(line)))  #in the form str"""
except FileNotFoundError as err:
    print ("file not found ")
    #if you want to  create the file if it doesnt exists then use the code given to create
    '''with open("Sample.text","xt") as fh:
    fh.write("hi this is sahil\n hope you doing good it was nice to meet you ")
    print("file created succesfully")
    '''
    
    
finally:
    print("completed successfully")
    #finally always runs

