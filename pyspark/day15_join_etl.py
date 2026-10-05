from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = SparkSession.builder.appName("joinetl").getOrCreate()

customer_df = spark.read.csv("datasets\\customers.csv", header = True)
orders_df = spark.read.csv("datasets\\orders.csv" , header=True)

df = customer_df.join(orders_df, on ="customer_id" ,how ="left")
print(customer_df.show(), orders_df.show())
df = df.withColumn("quantity", df["quantity"].cast("int"))
df = df.withColumn("price", df["price"].cast("int"))
df = df.withColumn("total_sale", df["quantity"]* df["price"])
print(df.filter(df["total_sale"]>= 50000).show())
print(df.groupBy("city").agg(F.sum("total_sale")).show())
df.orderBy("price").show()
df.orderBy(F.col("price").desc()).show()
print(df.show())