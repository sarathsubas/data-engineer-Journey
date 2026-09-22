import pandas as pd

with open("datasets\\sales_data.csv") as file:

    df = pd.read_csv(file)
    df["total_sale"]= df["quantity"] * df["price"]

    print(df)

    df["sale_level"] = df["total_sale"].apply(lambda x: "High" if x >= 100000 else( "Medium" if x>= 50000 else( "zero" if x==0 else "Low")))
  
    df["city"] = df["city"].str.upper()

    df["price_category"] = df["price"].apply(lambda x : "Expensive" if x >= 50000 else "Affordable")

    print(df[df["sale_level"]=="High"])
    print(df[df["sale_level"]=="Medium"])
    print(df[df["sale_level"]=="Low"])
    print(df[df["price_category"]=="Expensive"])
    print(df[df["price_category"]=="Affordable"])

    genral_dictionary = {'CHENNAI': 'CHN','BANGALORE': 'BLR','HYDERABAD': 'HYD','MUMBAI': 'MUM','GERMANY': 'GER'}
    df['city_code'] = df['city'].map(genral_dictionary)

    print(df)