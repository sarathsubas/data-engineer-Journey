try:
    with open("C:\\Learning\\data-engineer-Journey\\datasets\\sales_data2.csv", "r") as f1:
        print(f1.read())
except FileNotFoundError:
    print("File Not Found in the path")
else:
    print(f1.read())
