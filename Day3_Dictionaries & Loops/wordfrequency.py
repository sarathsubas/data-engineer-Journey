f = open("sample_file.txt","r+")
f.write("Apple\n")
f.write("Banana\n")
print(f.read())
f.close()

f = open("sample_file.txt","r+")
print(f.read())