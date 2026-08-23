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
        x =0 
        if columns[0] == "":
            x = 1
        order_id.append(columns[0])
        customer_name.append(columns[1])
        product.append(columns[2])
        category.append(columns[3])
        if int(columns[4]) <= 0:
            x=1
        quantity.append(columns[4])
        if int(columns[5]) <= 0:
            x=1
        price.append(columns[5])
        if columns[6] == "":
            x=1
        city.append(columns[6])
        if x ==1:
            x=0
            print(f"Invalid : {columns[0]}")
        else:
            print(f"Valid : {columns[0]}")