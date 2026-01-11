#area and perimeter of rectanglr
def area(length,breadth):
    return length*breadth
length=float(input("Enter the length"))
breadth=float(input("Enter the breadth"))
area(length,breadth)
print("Area=",area(length,breadth))

def perimeter(length,breadth):
    return 4*(length + breadth)
perimeter(length,breadth)
print("perimeter=",perimeter(length,breadth))