i =1
n = int(input("Enter the number of rows: "))
for _ in range(n):
     print(" " * (n - i), end="")
     print("* " * i)
     i=i+1