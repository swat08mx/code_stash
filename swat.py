import math
print(" Available functions are- + - * / ^  log (V1,V2,S1,S2) root ")
sign = input("Enter a sign: ")

if sign == "V1":
       S1 = input("Enter the value of S1: ")
       V2 = input("Enter the value of V2: ")
       S2 = input("Enter the value of S2: ")
       print((float(V2) * float(S2)) / float(S1))
elif sign == "V2":
       V1 = input("Enter the value of V1: ")
       S1 = input("Enter the value of S1: ")
       S2 = input("Enter the value of S2: ")
       print((float(V1) * float(S1)) / float(S2))
elif sign == "S1":
       V1 = input("Enter the value of V1: ")
       V2 = input("Enter the value of V2: ")
       S2 = input("Enter the value of S2: ")
       print((float(V2) * float(S2)) / float(V1))
elif sign == "S2":
       S1 = input("Enter the value of S1: ")
       V2 = input("Enter the value of V2: ")
       V1 = input("Enter the value of V1: ")
       print((float(V1) * float(S1)) / float(V2))



if sign == "^":
    num1 = input("Enter a number: ")
    power = input("Enter a power: ")
    print(int(num1) ** int(power))

elif sign == "log":
    num1 = input("Enter a number: ")
    print(math.log(int(num1)))

elif sign == "/":
    num1 = input("Enter a number: ")
    num2 = input("Enter another number: ")
    print(float(num1) / float(num2))
elif sign == "root":
    num1 = input("Enter a number to be sq rooted: ")
    print(math.sqrt(float(num1)))
    quit()
    

def twonum():
   if sign == "+":
    num1 = input("Enter a number: ")
    num2 = input("Enter another number: ")
    print(float(num1) + float(num2))

   elif sign == "-":
    num1 = input("Enter a number: ")
    num2 = input("Enter another number: ")
    print(abs(num1) - abs(num2))
   elif sign == "*":
    num1 = input("Enter a number: ")
    num2 = input("Enter another number: ")
    print(float(num1) * float(num2))
  

   else:
    print("Enter a valid operator")

def threenum():
    if sign == "+":
     num1 = input("Enter a number: ")
     num2 = input("Enter another number: ")
     num3 = input("Enter 3rd number: ")
     print(float(num1) + float(num2) + float(num3))

    elif sign == "-":
     num1 = input("Enter a number: ")
     num2 = input("Enter another number: ")
     num3 = input("Enter 3rd number: ")
     print(abs(num1) - abs(num2) - abs(num3))
    elif sign == "*":
     num1 = input("Enter a number: ")
     num2 = input("Enter another number: ")
     num3 = input("Enter 3rd number: ")
     print(float(num1) * float(num2) * float(num3))
    
    else:
     print("Enter a valid operator")

def fournum():
    if sign == "+":
     num1 = input("Enter a number: ")
     num2 = input("Enter another number: ")
     num3 = input("Enter 3rd number: ")
     num4 = input("Enter 4th number: ")
     print(float(num1) + float(num2) + float(num3) + float(num4))

    elif sign == "-":
     num1 = input("Enter a number: ")
     num2 = input("Enter another number: ")
     num3 = input("Enter 3rd number: ")
     num4 = input("Enter 4th number: ")
     print(abs(num1) - abs(num2) - abs(num3) - abs(num4))
    elif sign == "*":
     num1 = input("Enter a number: ")
     num2 = input("Enter another number: ")
     num3 = input("Enter 3rd number: ")
     num4 = input("Enter 4th number: ")
     print(float(num1) * float(num2) * float(num3) * float(num4))
    
    else:
     print("Enter a valid operator")

def fivenum():
    if sign == "+":
     num1 = input("Enter a number: ")
     num2 = input("Enter another number: ")
     num3 = input("Enter 3rd number: ")
     num4 = input("Enter 4th number: ")
     num5 = input("Enter 5th number: ")
     print(float(num1) + float(num2) + float(num3) + float(num4) + float(num5))

    elif sign == "-":
     num1 = input("Enter a number: ")
     num2 = input("Enter another number: ")
     num3 = input("Enter 3rd number: ")
     num4 = input("Enter 4th number: ")
     num5 = input("Enter 5th number: ")
     print(abs(num1) - abs(num2) - abs(num3) - abs(num4) - abs(num5))

    elif sign == "*":
     num1 = input("Enter a number: ")
     num2 = input("Enter another number: ")
     num3 = input("Enter 3rd number: ")
     num4 = input("Enter 4th number: ")
     num5 = input("Enter 5th number: ")
     print(float(num1) * float(num2) * float(num3) * float(num4) * float(num5))
    
    else:
     print("Enter a valid operator")




numbers = input("Enter number of numbers: ")
if numbers == "2":
    twonum()
elif numbers == "3":
    threenum()
elif numbers == "4":
    fournum()
elif numbers == "5":
    fivenum()







