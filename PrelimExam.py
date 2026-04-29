
def meal1(amount):
    if amount < price3:
        print("===========================")
        print("Your amount is insufficient")
        print("============================")
    else:
        print("============================")
        print("Your Meal set is: Meal 1")
        print(f"Your amount is: {amount}")
        print(f"Your change is: {amount- price1}")
        print("============================")

def meal2(amount):
    if amount < price3:
        print("===========================")
        print("Your amount is insufficient")
        print("============================")
    else:
        print("============================")
        print("Your Meal set is: Meal 2")
        print(f"Your amount is: {amount}")
        print(f"Your change is: {amount - price2}")
        print("============================")

def meal3(amount):
    if amount < price3:
        print("===========================")
        print("Your amount is insufficient")
        print("============================")
    else:
        print("============================")
        print("Your Meal set is: Meal 3")
        print(f"Your amount is: {amount}")
        print(f"Your change is: {amount - price3}")
        print("============================")

def meal4(amount):
    if amount < price3:
        print("===========================")
        print("Your amount is insufficient")
        print("============================")
    else:
        print("============================")
        print("Your Meal set is: Meal 4")
        print(f"Your amount is: {amount}")
        print(f"Your change is: {amount - price4}")
        print("============================")

def meal5(amount):
    if amount < price3:
        print("===========================")
        print("Your amount is insufficient")
        print("============================")
    else:
        print("============================")
        print("Your Meal set is: Meal 5")
        print(f"Your amount is: {amount}")
        print(f"Your change is: {amount - price5}")
        print("============================")

amount = 0
terminate = ""

price1 = 20
price2 = 30
price3 = 40
price4 = 50
price5 = 60

while terminate != "x":
    print("Do you want to order?\nPress Enter or any key to continue\nPress x to terminate ")
    terminate = input(": ")
    if terminate == "x":
        break
    print("============================")
    print("Meal 1 = 20\nMeal 2 = 30\nMeal 3 = 40\nMeal 4 = 50\nMeal 5 = 60")
    print("============================")
    select = int(input("Enter your Meal Set: "))
    amount = int(input("Enter your amount: "))

    if select == 1:
        meal1(amount)
    elif select == 2:
        meal2(amount)
    elif select == 3:
        meal3(amount)
    elif select == 4:
        meal4(amount)
    elif select == 5:
        meal5(amount)
    else:
        print("the menu you selected is not on the list.")

