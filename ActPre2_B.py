sumEven = 0

for x in range(1,11):
    if x % 2 == 0:
        sumEven += x
        continue
    elif x == 7:
        break
    else:
        print(x)

print(f"Sum of even numbers: {sumEven}")
