str1 = str(input("enter the values: "))
str2 = str(input("enter the values: "))
x=str1.lower()
y=str2.lower()
print(x)
print(y)
count=0
l=[]
for i in x:
    if i in y:
        print(i)
        #l.append(i)
        count+=1
    else:
        print("no")
print(count)
if count == len(y):
    print("anagram")
else:
    print("Not a anagram")

#-----------------------------------------
def is_anagram(s1, s2):
    # Remove spaces and convert to lowercase if necessary
    return sorted(s1.replace(" ", "").lower()) == sorted(s2.replace(" ", "").lower())

# Test
print(is_anagram("Schoolmastersi","The classroom is"))  # Output: True
print(is_anagram("rat", "tar"))    # Output: True
