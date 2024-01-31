n = int(input("Enter the no.of inputs :"))
names = []

for i in range(n):
    name = input("Enter the name :")
    names.append(name)
    names.sort()

for j in names:
    print(j)