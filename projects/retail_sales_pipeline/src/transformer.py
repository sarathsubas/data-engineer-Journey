def salessummary(column,data_bool):
    sales_summary =[]
    for x,y in zip(column,data_bool):
        if y==0:
            sales = int(x[4]) * int(x[5])
            sales_summary.append(sales)
    return sum(sales_summary)