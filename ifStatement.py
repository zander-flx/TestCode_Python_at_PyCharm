
age = int(input("Enter your age: "))

if age < 5:
    print(f"Learn some manners first")
elif 5 <= age < 18:
    print(f"Start Developing some skills")
elif 18 <= age < 50:
    print(f"Start looking for jobs")
elif 50 <= age < 80:
    print(f"Plan your retirement")
else:
    print(f"Retire already")
