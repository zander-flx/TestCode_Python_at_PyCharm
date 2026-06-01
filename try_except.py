#list of common exceptions: ValueError, ZeroDivisionError, TypeError, NameError, IndexError, FileNotFoundError

# try:
#     num = int(input("Enter a denominator: "))
#     print(f"10 divided by your denominator is: {10/num}")
#
# except ZeroDivisionError:
#     print("Cannot divide by zero.")
#
# except ValueError:
#     print("The number is not an integer.")
#
# except TypeError:
#     print("The input is not an integer.")

# try:
#     num = int(input("Enter a Denominator: "))
#     result = 10/num
#
# except ValueError:
#     print("The number you entered is not an integer.")
#
# except ZeroDivisionError:
#     print("Cannot divide by zero.")
#
# else:
#     print(f"10 divided by input is: {result}")

# try:
#     num = int(input("Enter a Denominator: "))
#     result = 10/num
#
# except ValueError:
#     print("The number you entered is not an integer.")
#
# except ZeroDivisionError:
#     print("Cannot divide by zero.")
#
# finally:
#     print("Program Finished")

# try:
#     file = open("D:/menu.txt","r")
#     print(file.read())
#
# except FileNotFoundError:
#     print("File not found.")
#
# finally:
#     print("Program Finished.")

# while True:
#     try:
#         num1 = int(input("Please enter first number: "))
#         num2 = int(input("Please enter second number: "))
#         answer = num1 + num2
#         print(f"{num1} + {num2} = {answer}")
#
#     except ValueError:
#         print("Please enter a valid number.")
#
#     except ZeroDivisionError:
#         print("Cannot divide by zero.")
#
#     repeat = True
#
#     while repeat:
#         choice = input('Would you like to try again? (y/n): ')
#         if choice.lower() == "y":
#             repeat = True
#             break
#         elif choice.lower() == "n":
#             repeat = False
#             break
#         else:
#             print("Please enter a valid choice.")
#
#     if repeat:
#         continue
#     else:
#         break

# age = int(input("Enter your age: "))
#
# if age <= 0:
#     raise ValueError("Your age cannot be lower than 0.")