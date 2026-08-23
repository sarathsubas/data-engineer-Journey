with open("datasets\\sales_data.csv", "r") as f1:
    order_id =[]
    customer_name =[]
    product =[]
    category=[]
    quantity=[]
    price=[]
    city=[]
    header = next(f1)
    f1.seek(0)
    list= f1.readline()
    for file in f1:
        columns = file.strip().split(",")
        order_id.append(columns[0])
        customer_name.append(columns[1])
        product.append(columns[2])
        category.append(columns[3])
        quantity.append(columns[4])
        price.append(columns[5])
        city.append(columns[6])


Total_Sales =[]
print(quantity,price)
for i,j,k in zip(quantity,price,product):
    print(f"{k} : {i} * {j}")
    Total_Sales.append(int(i) * int(j))
print (Total_Sales)
print (f"total_Sale : {sum(Total_Sales)}")

