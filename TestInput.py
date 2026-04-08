#input
fname = input("what is your first name?: ")
mname = input("what is your middle name?: ")
lname = input("what is your last name?: ")
age = int(input("How old are you?: "))
#Stored input is a string class, even if you typed a number
#You need to typecast the input to whatever variable you want.
print(f"Hello {fname} {mname} {lname}!")
print(f"You are {age} years old.")


