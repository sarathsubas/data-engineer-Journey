import pandas as pd

with open("datasets\\customers.csv") as file1:
    with open("datasets\\orders.csv") as file2:
        df_customer = pd.read_csv(file1)
        df_order = pd.read_csv(file2)

        print(df_customer)
        print(df_order)

        print(pd.merge(df_customer,df_order, on = 'customer_id', how='inner'))
        print(pd.merge(df_customer,df_order, on = 'customer_id', how='left'))
        print(pd.merge(df_customer,df_order, on = 'customer_id', how='right'))
        print(pd.merge(df_customer,df_order, on = 'customer_id', how='outer'))

        with open("datasets\\orders_january.csv") as file3:
            with open("datasets\\orders_february.csv") as file4:
                j_df = pd.read_csv(file3)
                f_df = pd.read_csv(file4)
                cat_jf =(pd.concat([j_df,f_df]))
                print(cat_jf)
                print(f"January_records: {j_df.shape[0]}")
                print(f"Febuary_records: {f_df.shape[0]}")
                print(f"total_records: {cat_jf.shape[0]}")