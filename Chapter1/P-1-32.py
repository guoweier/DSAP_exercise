# simulate a simple calculator

num1 = float(input("Enter the first number: "))
sign = input("Enter the operating sign: ")
num2 = float(input("Enter the second number: "))

if sign == "+":
    outcome = num1+num2
if sign == "-":
    outcome = num1-num2
if sign == "*":
    outcome = num1*num2
if sign == "/":
    if num2 == 0:
        outcome = "Divisor cannot be zero."
    else:
        outcome = num1/num2
print(int(outcome))