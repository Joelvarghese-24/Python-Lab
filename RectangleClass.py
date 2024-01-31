class rect():
    def __init__(self,l,b):
        self.l = l
        self.b = b

    def area(self):
        return self.l*self.b
    def perimeter(self):
        return 2 * (self.l+self.b)

l = int(input("Enter the length :"))
b = int(input("Enter the breadth :"))
obj = rect(l,b)
print("The area of rectangle is :",obj.area())
print("The perimeter of rectangle is :",obj.perimeter())