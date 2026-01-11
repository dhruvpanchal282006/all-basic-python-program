def convert(farenheit):
    return (farenheit-32)*5/9
farenheit=float(input("enter the farenheit"))
convert(farenheit)
print("celcius=",convert(farenheit))