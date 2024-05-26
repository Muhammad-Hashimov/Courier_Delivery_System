from helpers import connect as conn
from entities.admin import Admin
class Client(Admin):

    def __init__(self) -> None:
        pass

    def add_client(self, name, surname, age, number):
        sql = "Insert into client (Name, Surename, Age, Number) values (%s, %s, %s, %s)"
        conn.cursor.execute(sql, (name, surname, age, number))
        conn.connection.commit()