#rupees into dollars
def convert(rupees):
    return rupees//90
rupees=float(input("Enter the rupees"))
convert(rupees)
print("dollars=",convert(rupees ))