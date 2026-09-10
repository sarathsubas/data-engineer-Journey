import csv

with open("datasets\\sales_data.csv",'r') as file:
    content = csv.DictReader(file)
    header= content.fieldnames
    print(header)
    total_sale =[]
    for line in content:
        for x,y in line.items():
            print(f"{x} : {y}")
    file.seek(0)
    next(content)
    for line in content:
        total_sale.append(line['price'])
    print(f"total_sales: {sum(map(int, total_sale))}")