import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="raunak321",
  password="Raunak@321"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")