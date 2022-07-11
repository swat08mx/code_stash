print(" Available functions are- + - * / ^ ")
sign = input("Enter a sign: ")
num1 = input("Enter a number: ")
if sign == "^":
    power = input("Enter a power: ")
    print(int(num1) ** int(power))
else:
    num2 = input("Enter another number: ")

if sign == "+":
    print(float(num1) + float(num2))
elif sign == "-":
    print(float(num1) - float(num2))
elif sign == "*":
    print(float(num1) * float(num2))
elif sign == "/":
    print(float(num1) / float(num2))






