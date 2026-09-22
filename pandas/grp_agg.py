import pandas as pd

with open("datasets\\sales_data.csv") as file:

    df = pd.read_csv(file)
    print("========== SALES ANALYSIS ==========")

    df["total_sale"] = df["quantity"] * df["price"]
    
    print(df)
    print(f"total_sale : {sum(df["total_sale"])}")

    print("---------- CATEGORY-WISE SALES ----------")
    catagory_Sale =df.groupby('category').agg({"total_sale" :['sum'],
                                               "quantity":['sum'],
                                               "price": ['mean']})
    print(catagory_Sale)

    print("---------- CITY-WISE SALES ----------")
    city_Sale=df.groupby('city').agg({"total_sale" :['sum']})
    print(city_Sale)

    print("---------- PRODUCT SUMMARY ----------")

    product_sale = df.groupby('product').agg({"quantity":['sum'],
                                              "total_sale": ['sum']})
    print(product_sale)