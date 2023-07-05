[10:02 pm, 05/07/2023] Rimjhim: import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="msit"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers_51")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
[10:02 pm, 05/07/2023] Rimjhim: import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="msit"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM customers_students WHERE gender ='Male'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
[10:02 pm, 05/07/2023] Rimjhim: import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="msit"
)

mycursor = mydb.cursor()

sql = "DELETE FROM customers_students WHERE address = %s"
adr = ("Kolkata", )


mycursor.execute(sql, adr)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")