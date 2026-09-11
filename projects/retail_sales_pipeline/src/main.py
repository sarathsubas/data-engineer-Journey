import reader 
import validator
import transformer
import csv

path ="C:\\Learning\\data-engineer-Journey\\datasets\\sales_data.csv"
column = reader.read_sales_data(path)
print("================================\n"
           "RETAIL SALES PIPELINE\n"
        "================================")
print("\n")
print (f"Total Records: {len(column)}")
print(column)
print("\n")
sales_summary =[]
data_bool= validator.validation_data(column)
print("---------- VALIDATION ----------")
for i,j in zip(data_bool,column):
    if i == 0:
        print(f"{j[0]} -> Valid")
    else:
        print(f"{j[0]} -> Invalid")
print("\n")
print(f"Valid Records: {data_bool.count(0)}")
print(f"Invalid Records: {data_bool.count(1)}")

print ("\n---------- SALES SUMMARY ----------")

total_amount = transformer.salessummary(column,data_bool) 

print(f"total_amount: {total_amount}")

print ( "\n------------output csv------------")

output_Sales =[]
with open("projects\\retail_sales_pipeline\\output\\sales_output.csv","w") as file:
    sales_output = csv.writer(file)
    for i,j in zip(data_bool,column):
        if i == 0:
            output_Sales.append(j + [(int(j[4]) * int(j[5]))])
    for line in output_Sales:
        sales_output.writerow(line)
