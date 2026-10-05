from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.window import Window as W

spark = SparkSession.builder.appName("windowfn").getOrCreate()

df = spark.read.csv("datasets\\dirty_sales_data.csv" , header =True)

df = df.withColumn("quantity", df["quantity"].cast("int"))
df = df.withColumn("price", df["price"].cast("int"))
df = df.withColumn("total_sale", df["quantity"]* df["price"])

window_spec = W.partitionBy("category").orderBy(F.col("total_sale").desc())
df = df.withColumn("row_number", F.row_number().over(window_spec))
df= df.withColumn("rank",F.rank().over(window_spec))
df =df.withColumn("dense_rank", F.dense_rank().over(window_spec))
window_sp = W.partitionBy("category")
df = df.withColumn("category_total", F.sum("total_sale").over(window_sp))
df = df.withColumn("previous_sale", F.lag("total_sale").over(window_spec))
df.show()
