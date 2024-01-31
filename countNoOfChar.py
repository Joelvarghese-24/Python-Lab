string = input("Enter a string :")
count = 0

for i in range(len(string)):
    if i =='':
        continue
    else:
        count = count+1

print(count)