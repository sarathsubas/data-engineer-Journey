from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Basics").getOrCreate()


df = spark.read.csv(
    "datasets/sales_data.csv",
    header=True,
    inferSchema=True
)

print(df.show())
print(df.printSchema())
print(df.columns)
print(df.count())

df.select("product", "quantity", "price").show()

df.select("product").show()

df.filter(df["price"] > 50000).show()

df = df.withColumn(
    "total_sale",
    df["quantity"] * df["price"]
)


print(df.show())