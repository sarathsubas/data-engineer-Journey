import reader 
import validator

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

for x,y in zip(column,data_bool):
    if y==0:
        sales = int(x[4]) * int(x[5])
        sales_summary.append(sales)
print(f"Total Sales: {sum(sales_summary)}")