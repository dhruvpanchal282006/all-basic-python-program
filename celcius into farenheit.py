#celcius to farenheit
def convert(celcius):
    return (9/5*celcius) + 32
celcius=float(input("enter the celcius"))
convert(celcius)
print("farenheit=",convert(celcius))