import pandas as pd

with open("datasets\\sales_data.csv") as file:

    df = pd.read_csv(file)
    print("========== SALES ANALYSIS ==========")
    print(df.shape[0])

    df["total_sale"] = df["quantity"] * df["price"]

    print(df)
    print(f"total_sale : {sum(df["total_sale"])}")

    print("---------- CATEGORY-WISE SALES ----------")
    print(f"Electonic_sale: {sum(df["total_sale"][df["category"] == "Electronics"] )}")
    print(f"Accessories_sale: {sum(df["total_sale"][df["category"] == "Accessories"] )}")

    print("---------- CITY-WISE SALES ----------")
    print(f"chennai_sale: {sum(df["total_sale"][df["city"] == "Chennai"] )}")
    print(f"Bangalore_sale: {sum(df["total_sale"][df["city"] == "Bangalore"] )}")
    print(f"Hyderabad_sale: {sum(df["total_sale"][df["city"] == "Hyderabad"] )}")
    print(f"Mumbai_sale: {sum(df["total_sale"][df["city"] == "Mumbai"] )}")
    print(f"Germany_sale: {sum(df["total_sale"][df["city"] == "Germany"] )}")