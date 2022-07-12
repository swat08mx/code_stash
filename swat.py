import math
print(" Available functions are- + - * / ^  log (V1,V2,S1,S2) ")
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

elif sign == "^":
    num1 = input("Enter a number: ")
    power = input("Enter a power: ")
    print(int(num1) ** int(power))

elif sign == "log":
    num1 = input("Enter a number: ")
    print(math.log(int(num1)))


elif sign == "+":
    num1 = input("Enter a number: ")
    num2 = input("Enter another number: ")
    print(float(num1) + float(num2))

elif sign == "-":
    num1 = input("Enter a number: ")
    num2 = input("Enter another number: ")
    print(float(num1) - float(num2))
elif sign == "*":
    num1 = input("Enter a number: ")
    num2 = input("Enter another number: ")
    print(float(num1) * float(num2))
elif sign == "/":
    num1 = input("Enter a number: ")
    num2 = input("Enter another number: ")
    print(float(num1) / float(num2))

else:
    print("Enter a valid operator")







