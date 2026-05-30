
def meal1():
    if amount < price3:
        print("===========================")
        print("Your wallet amount is insufficient")
        print("============================")
    else:
        print("============================")
        print("Your Meal set is: Meal 1")
        print(f"Your wallet amount is: {amount}")
        print(f"Your change is: {amount- price1}")
        print("============================")

def meal2():
    if amount < price3:
        print("===========================")
        print("Your wallet amount is insufficient")
        print("============================")
    else:
        print("============================")
        print("Your Meal set is: Meal 2")
        print(f"Your wallet amount is: {amount}")
        print(f"Your change is: {amount - price2}")
        print("============================")

def meal3():
    if amount < price3:
        print("===========================")
        print("Your wallet amount is insufficient")
        print("============================")
    else:
        print("============================")
        print("Your Meal set is: Meal 3")
        print(f"Your wallet amount is: {amount}")
        print(f"Your change is: {amount - price3}")
        print("============================")

def meal4():
    if amount < price3:
        print("===========================")
        print("Your wallet amount is insufficient")
        print("============================")
    else:
        print("============================")
        print("Your Meal set is: Meal 4")
        print(f"Your wallet amount is: {amount}")
        print(f"Your change is: {amount - price4}")
        print("============================")

def meal5():
    if amount < price3:
        print("===========================")
        print("Your wallet amount is insufficient")
        print("============================")
    else:
        print("============================")
        print("Your Meal set is: Meal 5")
        print(f"Your wallet amount is: {amount}")
        print(f"Your change is: {amount - price5}")
        print("============================")

amount = 1
terminate = ""

price1 = 20
price2 = 30
price3 = 40
price4 = 50
price5 = 60

while terminate != "x":
    print("Do you want to order?\nPress any key to continue\nPress x to terminate ")
    terminate = input(": ")
    if terminate == "x":
        break
    print("============================")
    print("Meal 1 = 20\nMeal 2 = 30\nMeal 3 = 40\nMeal 4 = 50\nMeal 5 = 60")
    print("============================")
    select = int(input("Enter your Meal Set: "))
    amount = int(input("Enter your wallet amount: "))

    if select == 1:
        meal1()
    elif select == 2:
        meal2()
    elif select == 3:
        meal3()
    elif select == 4:
        meal4()
    elif select == 5:
        meal5()
    else:
        print("the menu you selected is not on the list.")
        continue

