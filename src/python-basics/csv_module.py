import csv

with open("datasets\\sales_data.csv",'r') as file:
    read_content = csv.reader(file)
    header = next(read_content)
    print(header)
    total_sale =[]
    for line in read_content:
            print(line)
            total_sale.append(int(line[5]))
    print(f"total_sales: {sum(total_sale)}")
    file.seek(0)
    row_count = sum(1 for line in read_content)

print(f"Total records: {row_count}")
    # with open("datasets\\sales_data2.csv",'w') as file:
    #     write_content = csv.writer(file)
    #     write_content.writerows(read_content)

