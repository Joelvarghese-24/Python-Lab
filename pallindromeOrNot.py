def pall(n):
    rev = int(str(n)[::-1])
    if(rev==n):
        return("Pallindrome")
    else:
        return("Not pallindrome")

num = int(input("Enter a number :"))
result = pall(num)
print(result)