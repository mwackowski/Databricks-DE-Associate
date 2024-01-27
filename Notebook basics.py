# Databricks notebook source
print('hello')

# COMMAND ----------

# MAGIC %sql
# MAGIC select "blblaa"

# COMMAND ----------

# MAGIC %md
# MAGIC # test
# MAGIC ## test2 

# COMMAND ----------

# MAGIC %run ./includes/Setup

# COMMAND ----------

print(full_name)

# COMMAND ----------

# MAGIC %fs ls '/databricks-datasets'

# COMMAND ----------

dbutils.help()

# COMMAND ----------

dbutils.fs.help()

# COMMAND ----------

files = dbutils.fs.ls('/databricks-datasets')

# COMMAND ----------

display(files)

# COMMAND ----------


