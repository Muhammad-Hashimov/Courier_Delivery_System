import mysql.connector
connection = mysql.connector.connect(user='root', password='hashimov19092004', host='127.0.0.1', database='courier')
cursor = connection.cursor(dictionary=True)