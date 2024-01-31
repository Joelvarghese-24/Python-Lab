print("Area of Triangle")
a = int(input("Enter side A : "))
b = int(input("Enter side B : "))
c = int(input("Enter side B :"))

s = (a+b+c)/2
area = (s*(s-a)*(s-b)*(s-c))**0.5
print("Area :",area)