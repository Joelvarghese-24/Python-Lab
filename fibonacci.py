def fib(i):
    if i <=1:
        return i
    else:
        return fib(i-1)+fib(i-2)

num = int(input("Enter a number :"))
print("Fibonacci series :")
for i in range(num):
    print(fib(i),end=' ')