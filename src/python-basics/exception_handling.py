print ("Enter the input: ")
a = input()
try:
    b = int(a)
except:
    print("Invalid number")   
else:
    print(f"Number: {b}")
finally:
    print("closing try.. except")

print ("Enter the inputs: ")
a = int(input())
b= int(input())
try:
    c = a/b 
except:
    print("Cannot divide by zero")   
else:
    print(f"Number: {b}")
finally:
    print("closing try.. except")
