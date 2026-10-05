from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = SparkSession.builder.appName("Report").getOrCreate()

df = spark.read.csv("datasets\\dirty_sales_data.csv",header=True)
print(df.show())
print(df.printSchema())
print(f"Number of total records: {df.count()}")


df= df.dropDuplicates()

df= df.fillna({'quantity' : 1, 'price' : 100000})

df= df.withColumn("customer_name",F.trim(df["Customer_name"]))
df = df.withColumn("city",F.upper(df["city"]))

df = df.withColumn("quantity", df["quantity"].cast("int"))
df = df.withColumn("price", df["price"].cast("int"))

df = df.withColumn("total_sale", df["quantity"] * df["price"])
df = df.withColumn(
    "sale_level",
    F.when(df["total_sale"] >= 100000, "High")
     .when(df["total_sale"] >= 50000, "Medium")
     .otherwise("Low")
)


print(df.filter(df["total_sale"]>50000).show())

print(df.groupBy("category").agg(
    F.sum("total_sale")
).show())

print(df.show())