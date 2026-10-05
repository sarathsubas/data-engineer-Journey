from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.window import Window  as W
spark = SparkSession.builder.appName("wndw").getOrCreate()

customer_df = spark.read.csv("datasets\\customers.csv", header = True)
orders_df = spark.read.csv("datasets\\orders.csv" , header=True)
df = customer_df.join(orders_df, on ="customer_id", how="left")

window_spec = W.orderBy(F.col("price").desc())

df =  df.withColumn("row_number",F.row_number().over(window_spec))
df =  df.withColumn("rank",F.rank().over(window_spec))
df =df.withColumn("Dense_rank",F.dense_rank().over(window_spec))
df.select("order_id", "product", "price", "row_number", "rank","Dense_rank").show()