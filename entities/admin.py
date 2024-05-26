from helpers import connect as conn
from helpers.integer import is_integer
class Admin():
    def __init__(self) -> None:
        self.people = []
        self.id = 0

    def add_courier(self, name: str, surname: str, number: str):
        sql = "insert into courier (Name, Surname, Number) values (%s, %s, %s)"
        while not number.isdigit():
            number = input("Please enter valid number: ")
        conn.cursor.execute(sql, (name, surname, number))
        conn.connection.commit()

    def show_couriers(self):
        sql = "select * from courier"
        conn.cursor.execute(sql)
        self.people = conn.cursor.fetchall()
        if len(self.people) == 0:
            print("There is not any courier")
            return []
        for i in range(len(self.people)):
            print(self.show_courier(self.people[i]["Name"], self.people[i]["Surname"], self.people[i]["Number"], i + 1))

    def show_courier(self, name, surname, number, id):
        return f'''
        --- {id} ---
        Name: {name}
        Surname: {surname}
        Number: {number}
        '''

    def delete_courier(self):
        self.show_couriers()
        if len(self.people) == 0:
            return
        ans = input("Please enter id of the courier that you want to delete: ")
        while not is_integer(ans) or int(ans) <= 0 or int(ans) > len(self.people):
            ans = input("Please enter valid id: ")
        self.id = int(ans) - 1
        sql = "delete from courier where id = %s"
        conn.cursor.execute(sql, (self.people[self.id]["Id"], ))
        conn.connection.commit()
        name = self.people[self.id]["Name"]
        surname = self.people[self.id]["Surname"]
        print(f"{name} {surname} is deleted succesfully")

    
    def delete_all_courier(self):
        sql = "truncate table courier"
        conn.cursor.execute(sql)
        conn.connection.commit()
        print("Couriers deleted succesfully")