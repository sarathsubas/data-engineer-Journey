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

with open("datasets\\sales_data1.csv","r") as f1:
    print(f1.read())