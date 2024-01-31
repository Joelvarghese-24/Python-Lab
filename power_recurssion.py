def pow(b,e):
    if(e==0):
        return 0;
    elif(e==1):
        return b
    else:
        return b * pow(b,e-1)

base = int(input("Enter the base value :"))
exponent = int(input("Enter the exponent value :"))
result = pow(base,exponent)
print(f"Result : {result}")