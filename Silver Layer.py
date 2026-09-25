# Databricks notebook source
from pyspark.sql.functions import *
from pyspark.sql.types import *

# COMMAND ----------

# MAGIC %md
# MAGIC # Silver Layer Script
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ### Data Access Using App

# COMMAND ----------

spark.conf.set("fs.azure.account.auth.type.awyuvadatalake.dfs.core.windows.net", "OAuth")
spark.conf.set("fs.azure.account.oauth.provider.type.awyuvadatalake.dfs.core.windows.net", "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider")
spark.conf.set("fs.azure.account.oauth2.client.id.awyuvadatalake.dfs.core.windows.net", "0629ff9c-f25a-4f06-bc1c-941a186a5166")
spark.conf.set("fs.azure.account.oauth2.client.secret.awyuvadatalake.dfs.core.windows.net", "jJ_8Q~Ol1jLyownUYCbKBD3n.EXjgHMAiXxG6adl")
spark.conf.set("fs.azure.account.oauth2.client.endpoint.awyuvadatalake.dfs.core.windows.net", "https://login.microsoftonline.com/d5d5cc17-b4c1-4dbd-a0a2-c8a80e515381/oauth2/token")

spark.conf.set(
    "fs.azure.account.oauth2.client.endpoint.awyuvadatalake.dfs.core.windows.net",
    "https://login.microsoftonline.com/d5d5cc17-b4c1-4dbd-a0a2-c8a80e515381/oauth2/token"
)


# COMMAND ----------

# MAGIC %md
# MAGIC ### Data Loading..

# COMMAND ----------

# MAGIC %md
# MAGIC ### Read All data

# COMMAND ----------

# DBTITLE 1,Cell 6

df_cal = spark.read.format('csv')\
            .option("header",True)\
            .option("inferSchema",True)\
            .load('abfss://bronze@awyuvadatalake.dfs.core.windows.net/AdventureWorks_Calendar')

# COMMAND ----------

df_cus = spark.read.format('csv')\
            .option("header",True)\
            .option("inferSchema",True)\
            .load('abfss://bronze@awyuvadatalake.dfs.core.windows.net/AdventureWorks_Customers')

# COMMAND ----------

df_pro_cat = spark.read.format('csv')\
            .option("header",True)\
            .option("inferSchema",True)\
            .load('abfss://bronze@awyuvadatalake.dfs.core.windows.net/AdventureWorks_Product_Categories')

# COMMAND ----------

df_pro_sub_cat = spark.read.format('csv')\
            .option("header",True)\
            .option("inferSchema",True)\
            .load('abfss://bronze@awyuvadatalake.dfs.core.windows.net/AdventureWorks_Product_Subcategories')

# COMMAND ----------

df_products = spark.read.format('csv')\
            .option("header",True)\
            .option("inferSchema",True)\
            .load('abfss://bronze@awyuvadatalake.dfs.core.windows.net/AdventureWorks_Products')

# COMMAND ----------

df_ret = spark.read.format('csv')\
            .option("header",True)\
            .option("inferSchema",True)\
            .load('abfss://bronze@awyuvadatalake.dfs.core.windows.net/AdventureWorks_Returns')

# COMMAND ----------

df_sales = spark.read.format('csv')\
            .option("header",True)\
            .option("inferSchema",True)\
            .load('abfss://bronze@awyuvadatalake.dfs.core.windows.net/AdventureWorks_Sales*')

# COMMAND ----------

df_territories = spark.read.format('csv')\
            .option("header",True)\
            .option("inferSchema",True)\
            .load('abfss://bronze@awyuvadatalake.dfs.core.windows.net/AdventureWorks_Territories')

# COMMAND ----------

# MAGIC %md
# MAGIC ### Transformations
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC #### Calendar Data

# COMMAND ----------

df_cal.display()

# COMMAND ----------

df_cal = df.withColumn('Month' ,month(col('Date')))\
            .withColumn('Year' ,year(col('Date')))
df_cal.display()
    

# COMMAND ----------

df_cal.write.format('parquet')\
            .mode('append')\
            .option("path",'abfss://silver@awyuvadatalake.dfs.core.windows.net/AdventureWorks_Calender')\
            .save()    
    

# COMMAND ----------

# MAGIC %md
# MAGIC #### Customers Data

# COMMAND ----------

df_cus.display()


# COMMAND ----------

# DBTITLE 1,Cell 22
df_cus = df_cus.withColumn('fullName',concat_ws(' ',col('Prefix'),col('FirstName'),col('LastName')))

# COMMAND ----------

df_cus.display()

# COMMAND ----------

df_cus.write.format('Parquet')\
            .mode('append')\
            .option("path",'abfss://silver@awyuvadatalake.dfs.core.windows.net/AdventureWorks_Customers')\
            .save()

# COMMAND ----------

# MAGIC %md
# MAGIC ### Product Categories

# COMMAND ----------

df_pro_cat.display()

# COMMAND ----------

df_pro_cat.write.format('Parquet')\
            .mode('append')\
            .option("path",'abfss://silver@awyuvadatalake.dfs.core.windows.net/AdventureWorks_Product_Categories')\
            .save()

# COMMAND ----------

# MAGIC %md
# MAGIC #### Product SubCategories

# COMMAND ----------

df_pro_sub_cat.display()

# COMMAND ----------

df_pro_sub_cat.write.format('Parquet')\
            .mode('append')\
            .option("path",'abfss://silver@awyuvadatalake.dfs.core.windows.net/AdventureWorks_Product_Subcategories')\
            .save()

# COMMAND ----------

# MAGIC %md
# MAGIC #### Products

# COMMAND ----------

df_products.display()

# COMMAND ----------

df_products.withColumn('ProductSKU',split(col('ProductSKU'),'-')[0])\
            .withColumn('ProductName',split(col('ProductName'),' ')[0])\
            .display()

# COMMAND ----------

df_products.write.format('Parquet')\
            .mode('append')\
            .option("path",'abfss://silver@awyuvadatalake.dfs.core.windows.net/AdventureWorks_Products')\
            .save() 

# COMMAND ----------

# MAGIC %md
# MAGIC #### Returns

# COMMAND ----------

df_ret.display()

# COMMAND ----------

df_ret.write.format('Parquet')\
            .mode('append')\
            .option("path",'abfss://silver@awyuvadatalake.dfs.core.windows.net/AdventureWorks_Returns')\
            .save() 

# COMMAND ----------

# MAGIC %md
# MAGIC #### Territories

# COMMAND ----------

df_territories.display()

# COMMAND ----------

df_territories.write.format('Parquet')\
            .mode('append')\
            .option("path",'abfss://silver@awyuvadatalake.dfs.core.windows.net/AdventureWorks_Territories')\
            .save() 

# COMMAND ----------

# MAGIC %md
# MAGIC #### Sales

# COMMAND ----------

df_sales.display()

# COMMAND ----------

df_sales = df_sales.withColumn('StockDate',to_timestamp('StockDate'))

# COMMAND ----------

df_sales = df_sales.withColumn('OrderNumber', regexp_replace('OrderNumber', 'S', 'T'))

# COMMAND ----------

df_sales = df_sales.withColumn('Multiply_LI&Q',col('OrderLineItem')*col('OrderQuantity'))

# COMMAND ----------

df_sales.display()

# COMMAND ----------

df_sales.write.format('Parquet')\
            .mode('append')\
            .option("path","abfss://silver@awyuvadatalake.dfs.core.windows.net/AdventureWorks_Sales")\
            .save()

# COMMAND ----------

# MAGIC %md
# MAGIC #### Sales Analysis
# MAGIC

# COMMAND ----------

df_sales.groupBy('OrderDate').agg(count('OrderNumber').alias('_Total_Orders')).display()

# COMMAND ----------

df_pro_cat.display()

# COMMAND ----------

df_territories.display()

# COMMAND ----------

