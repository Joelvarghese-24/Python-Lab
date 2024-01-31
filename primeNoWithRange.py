low = int(input("Enter the lower limit :"))
upp = int(input("Enter the upper limit :"))

for i in range(low,upp+1):
    if i>1:
        for j in range(2,i):
            if i%j == 0:
                break
        else:
            print(i)