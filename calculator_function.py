def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2
def mul(num1,num2):
    return num1*num2
def div(num1,num2):
    return num1/num2
def pow(num1,num2):
    return num1**num2

def calculator(num1,num2,opr):
    if opr == '+':
        return add(num1,num2)
    elif opr =='-':
        return sub(num1,num2)
    elif opr == '*':
        return mul(num1,num2)
    elif opr == '/':
        return div(num1,num2)
    elif opr == '**':
        return pow(num1,num2)
    else:
        return("Invalid input")

num1 = int(input("Enter first number :"))
num2 = int(input("Enter secound number : "))
operation = input("Choose an opeartion to perform (+ , - , * , / , **): ")
result = calculator(num1,num2,operation)
print(f"Result :{num1} {operation} {num2} = {result}")