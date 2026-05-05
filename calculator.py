#This is the first project to build a calculator.
while True:
 num1 = float(input("Enter the first number: "))
 num2 = float(input("Enter the second number: "))
#float() lets users enter decimals.

 operation = input("Enter the operation (+, -, *, /): ")
#Let users pick what they want to do.

 if operation == "+":
    result = num1 + num2
 elif operation == "-":
    result = num1 - num2
 elif operation == "*":
    result = num1 * num2
 elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero is not allowed."
 else:    result = "Error: Invalid operation."
#How python will respond.

 print("Result:", result)

 again = input("Do you want to perform another calculation? (yes/no): ")
 if again.lower() != "yes":
    break