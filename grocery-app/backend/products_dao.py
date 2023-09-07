import mysql.connector

cnx = mysql.connector.connect(user='root', password='Pray@#2010',
                              host='127.0.0.1',
                              database='shopsense')

cursor = cnx.cursor()
query = "SELECT * FROM shopsense.products"

cursor.execute(query)
cnx.close()