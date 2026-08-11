with open("datasets\\sales_data.csv", "r") as f1:
    header = next(f1)
    record_count = 0
    for line in f1:
        record_count += 1
    print(record_count)
    