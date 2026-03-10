# Check if the given string is a palindrom or not
a = str(input("Enter a string: "))
b = a[::-1]
if a == b:
    print("It is palindrom")
else:
    print("Not a Palindrom")
