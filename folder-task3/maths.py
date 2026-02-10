import math
num=float(input("enter the number "))
def sqr(num):
    if num<0:
        print("the function for this number dont exits")
    else:
        print(f"square root :{math.sqrt(num)} ")
def log(num):
    if num<=0:
        print("log doesnt exits ")
    else :
        print(f"natural log :{math.log(num)}")        
    
def sine(num):    
    print(f" sine :{math.sin(math.radians(num))}")
    
    
    
sqr(num)
log(num)
sine(num)
    
