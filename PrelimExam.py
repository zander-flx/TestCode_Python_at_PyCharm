
def meal1(amount):
    print("Your Meal set is: Meal 1")
    print(f"Your amount is: {amount}")
    print(f"Your payment is: {payment}")
    print(f"Your change is: {payment - price1 * amount}")

def meal2(amount):
    print("Your Meal set is: Meal 2")
    print(f"Your amount is: {amount}")
    print(f"Your payment is: {payment}")
    print(f"Your change is: {payment - price2 * amount}")

def meal3(amount):
    print("Your Meal set is: Meal 3")
    print(f"Your amount is: {amount}")
    print(f"Your payment is: {payment}")
    print(f"Your change is: {payment - price3 * amount}")

def meal4(amount):
    print("Your Meal set is: Meal 4")
    print(f"Your amount is: {amount}")
    print(f"Your payment is: {payment}")
    print(f"Your change is: {payment - price4 * amount}")

def meal5(amount):
    print("Your Meal set is: Meal 5")
    print(f"Your amount is: {amount}")
    print(f"Your payment is: {payment}")
    print(f"Your change is: {payment - price5 * amount}")

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
    print("Meal 1 = 20\nMeal 2 = 30\nMeal 3 = 40\nMeal 4 = 50\nMeal 5 = 60")
    select = int(input("Enter your Meal Set: "))
    amount = int(input("Enter your amount: "))
    payment = int(input("Enter your Payment: "))

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

