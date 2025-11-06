a = 12
b = bin(a)[2:]
while i >= 0:
    b = (i % 2) + b
    i = i // 2
    print ("the binary digit for ",a,"is",b)