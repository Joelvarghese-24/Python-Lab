l = int(input("Enter the length :"))
b = int(input("Enter the breadth :"))
area = lambda l,b: l+b
perimeter = lambda l,b: 2*(l+b)
print("The area of rectangle is:",area(l,b))
print("The of perimeter of rectangle is :",perimeter(l,b))