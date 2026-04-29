age = float(input("Enter your age: "))

if age < 0:
    print("Invalid age.")
elif 0 < age < 5:
    print("Learn some manners first")
elif 5 <= age < 18:
    print("Start Developing some skills")
elif 18 <= age < 50:
    print("Start looking for jobs")
elif 50 <= age < 80:
    print("Plan your retirement")
else:
    print("Retire already")
