from entities.client import Client
from entities.admin import Admin
from entities.delivery import Delivery
CL = Client()
AD = Admin()
DE = Delivery()
print("WELCOME to Courier Delivery System")
name = input("Please enter your name: ")
if name.lower() == "admin":
    password = input("Please enter admin's password: ")
    res = True
    while password != "12345":
        ans = input("This password is not right. Would you like try again? (Y | N): ")
        if ans == "Y" or ans == "y":
            password = input("Please enter admin's password: ") 
        else:
            res = False
            break
    if res:
        print('''
            Please enter admin operation:
              operations --- >
                1 -> Show all couries
                2 -> Delete all couriers
                3 -> Add courier
                4 -> Delete one courier
                exit -> Exit
        ''')
        while True:
            ans = input("Please enter your operation: ")
            if ans == "1":
                AD.show_couriers()
            elif ans == "2":
                AD.delete_all_courier()
            elif ans == "3":
                name = input("Please enter courier name: ")
                surname = input("Please enter courier surname: ")
                number = input("Please enter courier number: ")
                AD.add_courier(name, surname, number)
            elif ans == "4":
                AD.delete_courier()
            elif ans.lower() == "exit":
                print("SEE YOU AGAIN!")
                break
            else:
                print("Invalid operation")
            
else:
    surname = input("Please enter your surname: ")
    age = input("Please enter your age: ")
    if int(age) < 18:
        print("Your are not old enough to buy somothing. GET LOST !!!")
    else:
        number = input("Please enter your number: ")
        CL.add_client(name, surname, age, number)
        print('''
            Please enter client operation:
              operations --- >
                1 -> Show all items
                2 -> Add item
                exit -> Exit
        ''')
        while True:
            ans = input("Please enter your operation: ")
            if ans == "1":
                DE.show_items()
            elif ans == "2":
                id = input("Which one do you want to buy: ")
                DE.add_item(id)
                break
            elif ans.lower() == "exit":
                print("SEE YOU AGAIN!")
                break
            else:
                print("Invalid operation")