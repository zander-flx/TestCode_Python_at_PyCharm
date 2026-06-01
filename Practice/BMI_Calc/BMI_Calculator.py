from Person import Person
from Height import Height
from Weight import Weight


def calculate(weight_kg, height_m):
    bmi_calc = weight_kg / (height_m * height_m)
    return round(bmi_calc, 0)


def get_bmi(bmi_get):
    if bmi_get < 18:
        return "Underweight"
    elif 18.5 <= bmi_get < 25:
        return "Normal"
    elif 25 <= bmi_get < 30:
        return "Overweight"
    else:
        return "Obese"

while True:
    name = input("Enter your name: ")

    while True:
        try:
            weight_input = float(input("Enter your weight(kg): "))
            if weight_input <= 0:
                print("Weight cannot be zero or less")
                continue
            else:
                break
        except ValueError:
            print("Weight must be a number")
            continue

    while True:
        try:
            height_input = float(input("Enter your height(meter): "))
            if height_input <= 0:
                print("Height cannot be zero or less")
                continue
            else:
                break
        except ValueError:
            print("Height must be a number")

    person = Person(name)
    weight = Weight(weight_input)
    height = Height(height_input)

    bmi = calculate(weight.get_weight(), height.get_height())

    if bmi != 0:
        category = get_bmi(bmi)

        print("BMI RESULT")
        person.show_name()
        weight.show_weight()
        height.show_height()
        print(f"BMI: {bmi}")
        print(f"Category: {category}")
        break
    else:
        print("There's something wrong with your Height or Weight")
        continue
