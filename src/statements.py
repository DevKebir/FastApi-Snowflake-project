# create snowflake if not exist
st1 = "CREATE WAREHOUSE IF NOT EXISTS tiny_warehouse_mg"
st2 = "CREATE DATABASE IF NOT EXISTS testdb_mg"
st3 = "USE DATABASE testdb_mg"
st4 = "CREATE SCHEMA IF NOT EXISTS testschema_mg"

# use earlier created schema
u1 = "USE WAREHOUSE tiny_warehouse_mg"
u2 = "USE DATABASE testdb_mg"
u3 = "USE SCHEMA testdb_mg.testschema_mg"

# create table  in the current schema
t1 = "create table if not exists testdb_mg.testschema_mg.Product (Id integer, Name varchar, Price double, primary key(Id))"

# API queries
q1 = "SELECT * FROM testdb_mg.testschema_mg.product"
q3 = "SELECT Name, Price FROM testdb_mg.testschema_mg.product where id = %s"
q2 = "SELECT * from  testdb_mg.testschema_mg.product where Name = %s limit 5;"
# get last record
q4 = "SELECT * FROM testdb_mg.testschema_mg.product Order BY ID DESC LIMIT 1"


# insert data into table
i1 = "INSERT INTO testdb_mg.testschema_mg.product (Id, Name, Price) VALUES (%s,%s,%s)"

# update data
u1 = "UPDATE testdb_mg.testschema_mg.product SET Name =%s, Price=%s WHERE id=%s"

# delete data from table
d1 = "DELETE FROM testdb_mg.testschema_mg.product WHERE id=%s"
