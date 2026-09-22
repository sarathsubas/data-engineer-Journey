import pandas as pd

with open("datasets\\dirty_sales_data.csv") as file:

    df = pd.read_csv(file)

    print("========== DATA CLEANING REPORT ==========")

    print(df.isnull().sum())

    rem_dro = df.dropna()
    print(rem_dro)

    ad_fil = df.fillna(0)
    print(ad_fil)

    print(f"Duplicate Records: {df.duplicated().sum()}")

    df = df.drop_duplicates()
    print(df)

    df["customer_name"] = df["customer_name"].str.strip()
    df["city"] = df["city"].str.strip()
    df["city"] = df["city"].str.lower()
    

    df["quantity"] = df["quantity"].fillna(0).astype(int)
    df["price"] = df["price"].fillna(0).astype(int)
    print("---------- CLEANED DATA ----------")
    print(df)

    print(f"Final_record_count : {df.shape[0]}")