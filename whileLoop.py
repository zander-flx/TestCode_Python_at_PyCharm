count = 0

while count <= 10:
    count += 1
    if count == 4:
        continue#skips the number 4
    elif count == 9:
        break#breaks loop when count is 9
    print(count, end=", ")

