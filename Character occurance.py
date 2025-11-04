a = input("Enter a word:")
b = input("Enter a character:")
i = 0
j = 0
while (i < len(a)):
    if (a[i] == b):
     j = j + 1
    i = i + 1
print ("the number of character given is",j,"in the word given:",a)