import pandas as pd

with open("datasets\\sales_data.csv") as file:

    df = pd.read_csv(file)
    print(df)
    
    print("========== SALES INSIGHTS REPORT ==========")
    print(f"Total Records: {df.shape[0]}")
    df["total_Sale"] = df["quantity"] * df["price"] 

    cnt = df.value_counts("category")
    print(cnt)
    
    cntcit = df.value_counts("city")
    print(cntcit)
    
    print("---------- TOP SALES ----------")

    sorti = df.sort_values("price")
    print(sorti)
    
    sordes = df.sort_values("total_Sale",ascending=False )
    print(sordes)

    print("---------- HIGH VALUE ELECTRONICS ----------")
    rec_fil = df[(df["category"]=="Electronics")&(df["price"]>50000)]
    print (rec_fil)

    rec_fil1 = df[(df["city"]=="chennai") | (df["city"]=="Bangalore")]
    print(rec_fil1)

    print("---------- SELECTED CITIES ----------")
    indata = df[(df["city"].isin(["Chennai", "Mumbai", "Germany"]))]
    print(indata)

    print("----------RECORD COUNT ----------")

    unirec = df["product"].nunique()
    print(f"product_record_count: {unirec}")

    unicit = df["city"].nunique()
    print(f"city_Reccordd_count: {unicit}")

    uniCus = df["customer_name"].nunique()
    print(f"customer_name: {uniCus}")