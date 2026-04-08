def voltage(val1, val2):
    return val1 * val2

def ampere(val1, val2):
    return val1 / val2

def resistance(val1, val2):
    return val1 / val2

val1 = float(input("Enter value1: "))
val2 = float(input("Enter value2: "))

volts = voltage(val1, val2)
amps = ampere(val1, val2)
resis = resistance(val1, val2)

print(f"Voltage = {volts}")
print(f"Ampere = {amps}")
print(f"Resistance = {resis}")

