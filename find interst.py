#find interst
def findinterest(p,r,n):
    return p*r*n/1000
p=float(input("Enter the principal amount"))
r=float(input("Enter the rate"))
n=float(input("Enter the no of years"))
findinterest(p,r,n)
print("interst=",findinterest(p,r,n))