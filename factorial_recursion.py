def fact(n):
    if n <=1 :
        return n
    else:
        return n *fact(n-1)

num = int(input("Enter a number :"))
result = fact(num)
print(f"Factorial of {num} is {result}")