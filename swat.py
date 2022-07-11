num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
sign = input("Enter a sign: ")


if sign == "+":
    print(float(num1) + float(num2))
elif sign == "-":
    print(float(num1) - float(num2))
elif sign == "*":
    print(float(num1) * float(num2))
elif sign == "/":
    print(float(num1) / float(num2))
else:
    print("Sign is invalid")
while num2 > num1:
    print(num2)
    num2=num2-1.57






