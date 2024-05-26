from helpers.foods import foods
from helpers.integer import is_integer

class Delivery:
    def __init__(self):
        pass

    def show_items(self):
        for food in foods:
            print(self.show_item(foods[food][0],foods[food][1],food))

    def show_item(self, name, price, id):
        return f"{id}. {name} --->  {price} AZN"
    
    def add_item(self, id: int):
        total = 0
        while not is_integer(id) or int(id) <= 0 or int(id) > len(foods):
            id = input("Please enter valid id: ")
        total += foods[int(id)][1]
        ans = input(f"{foods[int(id)][0]} is added to basket. Do you want to add something else (Y | N): ")
        while ans == "Y" or ans == "y":
            id = input("Which one do you want to buy: ")
            while not is_integer(id) or int(id) <= 0 or int(id) > len(foods):
                id = input("Please enter valid id: ")
            total += foods[int(id)][1]
            ans = input(f"{foods[int(id)][0]} is added to basket. Do you want to add something else (Y | N): ")
        else:
            res = input(f"Total amount is {total} AZN. Do you want to buy? (Y | N): ")
            if res == "Y" or res == "y":
                print(f"Your delivery is coming. Your bill will be {total} AZN")
                return