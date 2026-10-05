from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = SparkSession.builder.appName("day16").getOrCreate()

customer_df = spark.read.csv("datasets\\customers.csv", header = True)
orders_df = spark.read.csv("datasets\\orders.csv" , header=True)

df = customer_df.join(orders_df, on= 'customer_id' , how= "Left")
df.show()

asc = df.orderBy("price")
desc = df.orderBy(F.col("price").desc())

asc.show()
desc.show()

qnty = df.orderBy("quantity")
desc_qnty = df.orderBy(F.col("quantity").desc())

qnty.show()
desc_qnty.show()