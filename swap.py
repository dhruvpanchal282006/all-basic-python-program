def swap(a,b):
    temp=a
    a=b
    b=temp
    return a,b
x=int(input("Enter the values of first number"))
y=int(input("Enter the value of second number"))
x,y=swap(x,y)
print("x=",x)
print("y=",y)