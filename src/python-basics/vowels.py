# This is program to count vowels in a string

def count_vowels(a):
    count = 0
    for i in a:
        if i in "aeiouAEIOU":
            count += 1
    return count


string = str(input("Enter the string:"))
count = count_vowels(string)
print("Number of vowels in the string is:", count)
