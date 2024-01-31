y = {}
l = []
n = int(input("Enter the no.of students :"))

for i in range(n):
    name = input("Enter the name :")
    age = int(input("Enter the age :"))
    y[name] = age

l = list(y.items())
l.sort()
print("sorting in ascending order :")
a = dict(l)
print(a)
print("Sorting in descending order :")
l.sort(reverse=True)
dic = dict(l)
print(dic)