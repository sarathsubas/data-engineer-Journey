import pandas as pd

with open("datasets\\dirty_sales_data.csv") as file:
    df = pd.read_csv(file)
    print(df)
    print("========== ETL PIPELINE ==========")
    print("Extracting data...")
    print(f"Records extracted: {df.shape[0]}")
    print("---------- DATA QUALITY ----------")
    print(df.isnull().sum())
    dup_rec = df[df.duplicated()]
    print("Duplicate records")
    print(dup_rec)
    print(f"Number of records : {dup_rec.shape[0]}")
    print("---------- DATA CLEAN ----------")
    df_1 = df.drop_duplicates()
   
    df_1 = df_1.fillna({"quantity" :1})
    df_1 = df_1.fillna({"price" : 10000})
    df_1["customer_name"] = df_1["customer_name"].str.strip()
    df_1["city"] = df_1["city"].str.strip()
    df_1["city"] = df_1["city"].str.upper()
    print(f"Cleaned records: {df_1.shape[0]}")

    print("---------- DATA TRANSFORM ----------")
    df_1["total_sale"] = df_1["quantity"] * df_1["price"]
    df_1["sale_level"] = df_1["total_sale"].apply( lambda x : "high" if x>= 100000 else ("Medium" if x>= 50000 else "Low"))
    df_1["city_code"] = df_1["city"].map({"CHENNAI" : "CHN","BANGALORE" : "BLR", "HYDERABAD" : "HYD", "GERMANY" : "DE","MUMBAI" : "BOM"})
    df_1["price_category"] = df_1["price"].apply(lambda x : "Expensive" if x >= 50000 else "Affordable")
    print(df_1)

    print("---------- DATA ANALYSIS ----------")
    Category_wisesale = df_1.groupby('category').agg({"total_sale" : ['sum']})
    city_wisesale = df_1.groupby('city').agg({"total_sale" : ['sum']})
    Product_wisesale = df_1.groupby('product').agg({"quantity" :['sum'],
                                                    "total_sale" : ['sum']})

    print(f"Category_wisesale : {Category_wisesale}")
    print(f"city_wisesale : {city_wisesale}")
    print(f"Product_wisesale : {Product_wisesale}")

    print("---------final_output----------")
    df_1.to_csv('outputs\\sales_etl_output.csv', index=False)