str1 = str(input("enter the values: "))
str2 = str(input("enter the values: "))
x=str1.lower()
y=str2.lower()
print(x)
print(y)
count=0
for i in x:
    if i in y:
        print(i)
        count+=1
    else:
        print("no")
print(count)
if count == len(y):
    print("anagram")
else:
    print("Not a anagram")