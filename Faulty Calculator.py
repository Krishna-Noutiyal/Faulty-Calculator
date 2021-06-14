"""
Creating a Faulty calculator
which gives wrong result for 

45 * 3 = 555, 56+9 = 77, 56/6 = 4
"""
# Ask user for and operator in input
from os import error


print("Enter the operator you want to use like (/ + * -)\n")

#  Stores the user input as string
ort = input()

#  if else condition runs if the input is *
if ort=="*":
    
    # Ask for 1st number
    print("\nEnter the 1st number\n")
    num1 = int(input())

    # Ask for 2nd number
    print("Enter the 2nd number\n")
    num2 = int(input())

    # Fault error if 1st number and 2nd number are 45 and 3
    if num1 == 45 and num2 == 3 :
        n = 555
        print("The answer is", n)
    elif num1 == 3 and num2 == 45 :
        n = 555
        print("The answer is", n)
    # if the number are diffrent normal calculation occur
    else:
        print("The answer is", num1 * num2)

elif ort=="+":
    
    print("\nEnter the 1st number\n")
    num1 = int(input())

    print("Enter the 2nd number\n")
    num2 = int(input())

    if num1 == 56 and num2 == 9 :
        n = 77
        print("The answer is", n)
    elif num1 == 9 and num2 == 56 :
        n = 77
        print("The answer is", n)
    else:
        print("The answer is", num1 + num2)

elif ort=="/":
    
    print("\nEnter the 1st number\n")
    num1 = int(input())

    print("Enter the 2nd number\n")
    num2 = int(input())

    if num1 == 56 and num2 == 6 :
        n = 4
        print("The answer is", n)
    else:
        print("The answer is", num1 / num2)

elif ort=="-":
    
    print("\nEnter the 1st number\n")
    num1 = int(input())

    print("Enter the 2nd number\n")
    num2 = int(input())

    print("The answer is", num1-num2)

# if operatior is not * + / 
# subtraction occur
else :
    print("\nEnter the 1st number\n")
    num1 = int(input())

    print("Enter the 2nd number\n")
    num2 = int(input())
    print("The answer is", num1 - num2)

# To stop the python program window until user press enter
z = "\nPress enter to exit"
print (z)
exit = input()



