from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder \
    .appName("Netflix Analysis") \
    .getOrCreate()

df = spark.read.csv(
    "netflix_titles.csv",
    header=True,
    inferSchema=True
)

print("Primeros registros")
df.show(5)

print("Estructura")
df.printSchema()

print("Total de registros")
print(df.count())

print("Películas y series")
df.groupBy("type").count().show()

print("Contenido por clasificación")
df.groupBy("rating").count().show()

print("Top 10 años con más contenido")
df.groupBy("release_year") \
  .count() \
  .orderBy(col("count").desc()) \
  .show(10)

print("Top países")
df.groupBy("country") \
  .count() \
  .orderBy(col("count").desc()) \
  .show(10)

print("Películas posteriores a 2015")
df.filter(col("release_year") > 2015).show(10)

spark.stop()
