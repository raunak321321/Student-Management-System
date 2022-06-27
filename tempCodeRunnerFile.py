import mysql.connector as mysql_db

# making Connection
# con = mysql_db.connect(host="localhost",user="root", password="")
con = mysql_db.connect(host="localhost",user="root", password="",database="employee")

# print(con)

mycursor = con.cursor()

# mycursor.execute("create database employee")

mycursor.execute("Create table empdata (ID BIGINT primary key,name varChar(1000),emailID text(1000), phoneNO BIGINT,address text(1000),post text(1000),salary BIGINT)")