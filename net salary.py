def netsalary(grossamount,allowance,deduction):
    return grossamount-deduction+allowance
grossamount=float(input("Enter the gross amount"))
deduction=float(input("Enter the deduction"))
allowance=float(input("Enter the allowance"))
netsalary(grossamount,deduction,allowance)
print("netsalary=",netsalary(grossamount,allowance,deduction))