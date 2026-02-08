num=int(input("enter the number "))

def factorial(num):
    if num==0 or num==1:
        return 1
    elif num<0:
        print("enter the correct value ")
    else :
        return num*factorial(num-1)
    
print(f"the factorial of {num} is  {factorial(num)}")