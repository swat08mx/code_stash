import math
print(" Available functions are- + - * / ^  log")
sign = input("Enter a sign: ")
num1 = input("Enter a number: ")

if sign == "^":
    power = input("Enter a power: ")
    print(int(num1) ** int(power))

elif sign == "log":
       print(math.log(int(num1)))


elif sign == "+":
       num2 = input("Enter another number: ")
       print(float(num1) + float(num2))
elif sign == "-":
       num2 = input("Enter another number: ")
       print(float(num1) - float(num2))
elif sign == "*":
       num2 = input("Enter another number: ")
       print(float(num1) * float(num2))
elif sign == "/":
       num2 = input("Enter another number: ")
       print(float(num1) / float(num2))

else:
    print("Enter a valid operator")







