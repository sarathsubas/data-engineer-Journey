f= open("datasets\\sales_data.csv","r")
print(f.read())
f.seek(0)
print(f.readline())
f.seek(0)
print(f.readlines())

f= open("datasets\\sales_data1.csv","w")
f.write("order_id,customer_name,product,category,quantity,price,city")
f.close()

with open ("datasets\\sales_data1.csv","a") as file:
    file.write("\n1004,Sarath,PS5,Accessories,2,50000,Mumbai")

with open("datasets\\sales_data.csv","r") as f1:
    header = next(f1)
    word_count=0
    for words in f1:
        count = words.split()
        word_count += len(words)
    print(f1.read())
    print(word_count)