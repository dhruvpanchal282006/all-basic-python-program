#conversion of bytes
def convert(bytes):
    return bytes/1024
    return kilobytes/1024
    return megabytes/1024
bytes=float(input("Enter the bytes"))
convert(bytes)
print("kilobytes=",convert(bytes))
print("megabytes=",convert(bytes))
print("gigabytes=",convert(bytes))