num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
aws = num1 * num2

print(str(num1) + " x " + str(num2) + " = " + str(aws))
if aws > 0:
    print("The result is positive.")
elif aws < 0:
    print("The result is negative.")
else:
    print("The result is positive and negative.")
