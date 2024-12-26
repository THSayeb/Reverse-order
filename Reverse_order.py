print("\nDigits counter")
num = int(input("Enter a number "))
int1 = num

i = 0
while int1 > 0:
    int1 //= 10
    i += 1

print("\nThe given number has ", i, "digits")