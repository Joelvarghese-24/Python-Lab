num1 = float(input("Enter the first number : "))
num2 = float(input("Enter the secound number : "))
operation  = input("Choose an operation to perform(+ , - , * , / , ** , %) : ")
print("The result of arithmetic operation is : ")
if operation == '+':
    result = num1+num2
    print(f"{num1} + {num2} = {result}")
elif operation == '-':
    result = num1-num2
    print(f"{num1} - {num2} = {result}")
elif operation == '*':
    result = num1*num2
    print(f"{num1} x {num2} = {result}")
elif operation == '/':
    result = num1/num2
    print(f" {num1} / {num2} = {result}")
elif operation == '**':
    result = num1 ** num2
    print(f" {num1} ** {num2} = {result}")
elif operation == '%':
    result = num1 % num2
    print(f" {num1} % {num2} = {result}")
else:
    print("Invalid Inputs")