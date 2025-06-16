total_bill = 0
menu = {
    "majestic": 250,
    "drumstick": 210,
    "kebab": 350,
    "biryani": 450,
    "water bottle": 30
}

dish_one_choice = input("What do you want?  ") 
dish_one_quantity = int(input("How many?  ")) 

dish_two_choice = input("What do you want?  ")
dish_two_quantity = int(input("How many?  "))

dish_one_bill = (dish_one_quantity * menu.get(dish_one_choice))
dish_two_bill = (dish_two_quantity * menu.get(dish_two_choice))

total_bill =  dish_one_bill + dish_two_bill

detailed_bill = f"""

#####WELCOME TO SO AND SO HOTEL######
BILL ID: {total_bill * 32}

{dish_one_choice} X {menu.get(dish_one_choice)} = {dish_one_bill}
{dish_two_choice} X {menu.get(dish_two_choice)} = {dish_two_bill}
-------------------------------------------------------------------
GST: 0%
TAXES: 0%
------------------------------------TOTAL BILL: Rs.{total_bill}/----

THANKS FOR VISITING US

"""

print(detailed_bill)