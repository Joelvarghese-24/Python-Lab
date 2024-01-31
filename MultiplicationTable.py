a = int(input("Enter a number : "))
limit = int(input("Enter the limit : "))
i = 1
print(f"Multiplication table of {a} is :")
while(i<=limit):
    m = a*i
    print(f"{a} x {i} = {m}")
    i = i+1
