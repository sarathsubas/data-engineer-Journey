import csv

with open("datasets\\sales_data.csv",'r') as file:
    read_content = csv.reader(file)

    # with open("datasets\\sales_data2.csv",'w') as file:
    #     write_content = csv.writer(file)
    #     write_content.writerows(read_content)

with open("datasets\\sales_data.csv",'r') as file:
    content = csv.DictReader(file)
    header= content.fieldnames
    print(header)
    for line in content:
        print(line['order_id'])