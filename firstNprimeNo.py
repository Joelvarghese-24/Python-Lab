n = int(input("Enter the limit :"))
c = 2

while(n!=0):
    for i in range(2,c):
        if(c%i)==0:
            break
    else:
        print(c,end=' ')
        n = n-1
    c = c+1