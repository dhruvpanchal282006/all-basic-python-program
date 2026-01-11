def netsales(totalsales,retur,discount):
    return totalsales-retur-discount
totalsales=float(input("Enter the totalsales"))
retur=float(input("Enter the return"))
discount=float(input("Enter the discount"))
netsales(totalsales,retur,discount)
print("netsales=",netsales(totalsales,retur,discount))