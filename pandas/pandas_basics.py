import pandas as pd

with open ("datasets\\sales_data.csv", "r") as file:

    df = pd.read_csv(file)
    print(df.head())
    print(df.to_string())
    print(df.tail())
    print(df.shape)
    print(df.columns)
    print(df.info())
    print(df.describe())
    print(df["product"])

    print(df[["product", "quantity", "price"]])

    print(df[df["quantity"]>1] )
    print(df[df["price"] >= 50000] )
    print(df[df["category"] == "Electronics"] )
  