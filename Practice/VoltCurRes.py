from voltage import Voltage
from current import Current
from resistance import Resistance

v = float(input("Enter Voltage: "))
a = float(input("Enter Current: "))
r = float(input("Enter Resistance: "))

voltage1 = Voltage(v)
current1 = Current(a)
resistance1 = Resistance(r)

print("="*17)
print("Electrical Values")
print("="*17)

voltage1.show_voltage()
current1.show_current()
resistance1.show_resistance()