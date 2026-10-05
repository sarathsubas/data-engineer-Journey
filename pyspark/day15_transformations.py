from pyspark.sql import SparkSession
from pyspark.sql import functions as F
spark = SparkSession.builder.appName("day15").getOrCreate()

df = spark.read.csv("datasets\\dirty_sales_data.csv" , header =True)

df= df.withColumn("quantity",df["quantity"].cast("int"))
df = df.withColumn("price", df["price"].cast("int"))

df = df.withColumn("total_sale", df["quantity"]*df["price"])
df = df.withColumn("sale_level", F.when (df["total_sale"] >= 100000 , "High")
                   .when (df["total_sale"]>= 50000 ,"Medium")
                    .otherwise("low"))
df = df.withColumn("city", F.upper(df["city"]))
df = df.withColumn("city", F.trim(df["city"]))
df = df.withColumn("customer_name", F.trim(df["customer_name"]))

city_mapping = F.create_map(
    F.lit("CHENNAI"), F.lit("CHN"),
    F.lit("BANGALORE"), F.lit("BLR"),
    F.lit("HYDERABAD"), F.lit("HYD"),
    F.lit("MUMBAI"), F.lit("BOM"),
    F.lit("GERMANY"),F.lit("DE")
)
df = df.withColumn("city_code", city_mapping[ df["city"]])

df= df.withColumn("order_size", F.when(df["quantity"]>= 3 ,"Large")
                  .when(df["quantity"]>= 2 ,"Medium")
                  .otherwise("Small"))

sale = df.filter(df["total_sale"]>50000)
catee = df.filter(df["category"] == "Electronics")
elec = df.filter((df["category"] == "Electronics") & (df["total_sale"]>50000))
print(sale.show())
print(catee.show())
print(elec.show())
print(df.groupBy("category").agg(F.sum("total_sale")).show())
print(df.show())

customer_pd = spark.read.csv("datasets\\customers.csv", header=True)
orders_pd = spark.read.csv("datasets\\orders.csv", header=True)

print(customer_pd.join( orders_pd, on="customer_id" ,how="inner").show())
print(customer_pd.join(orders_pd , on="customer_id" , how="left").show())
print(customer_pd.join(orders_pd , on="customer_id" , how="right").show())
print(customer_pd.join(orders_pd , on="customer_id" , how="outer").show())