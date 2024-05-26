import mysql.connector
conn = mysql.connector.connect(user='root', password='hashimov19092004', host='127.0.0.1', database='courier')
cursor = conn.cursor()
class Courier:
    def __init__(self):
        pass


    def add_person(self,name,surename,age,number):
        sql = "insert into client (Name, Surename, Age, Number) values ( %s,%s, %s, %s)"
        cursor.execute(sql, (name, surename, age, number))
        conn.commit()
#     def save_to_db(self):
#         try:
#             conn = mysql.connector.connect(user='root', password='hashimov19092004', host='127.0.0.1', database='courier')
#             cursor = conn.cursor()
#             if self.id is None:
#                 query = "INSERT INTO couriers (name, phone) VALUES (%s, %s)"
#                 cursor.execute(query, (self.name, self.phone))
#                 self.id = cursor.lastrowid
#             else:
#                 query = "UPDATE couriers SET name=%s, phone=%s WHERE id=%s"
#                 cursor.execute(query, (self.name, self.phone, self.id))
#             conn.commit()
#         except mysql.connector.Error as err:
#             print(f"Error: {err}")
#         finally:
#             cursor.close()
#             conn.close()

#     @staticmethod
#     def get_all_couriers():
#         try:
#             conn = mysql.connector.connect(user='root', password='password', host='127.0.0.1', database='courier_db')
#             cursor = conn.cursor()
#             query = "SELECT * FROM couriers"
#             cursor.execute(query)
#             results = cursor.fetchall()
#             return results
#         except mysql.connector.Error as err:
#             print(f"Error: {err}")
#         finally:
#             cursor.close()
#             conn.close()

#     @staticmethod
#     def delete_courier(courier_id):
#         try:
#             conn = mysql.connector.connect(user='root', password='password', host='127.0.0.1', database='courier_db')
#             cursor = conn.cursor()
#             query = "DELETE FROM couriers WHERE id=%s"
#             cursor.execute(query, (courier_id,))
#             conn.commit()
#         except mysql.connector.Error as err:
#             print(f"Error: {err}")
#         finally:
#             cursor.close()
#             conn.close()

