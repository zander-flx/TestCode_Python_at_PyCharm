Age = int(input("Enter your age: "))

if Age < 3:
    print(f"Learn some manners first")
if 3 <= Age < 18:
    print(f"Start Developing some skills")
elif 18 <= Age < 50:
    print(f"Start looking for jobs")
elif 50 <= Age < 80:
    print(f"Plan your retirement")
else:
    print(f"Retire already")