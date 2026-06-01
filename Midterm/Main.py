from Employee import Employee
from Salary import Salary
from Payroll import Payroll

def compute(hours, rate):
    egross = hours * rate
    return egross

while True:
    n = input("Enter Employee Name: ")
    s = input("Enter Employee Status: ")
    while True:
        try:
            h = float(input("Enter Employee Hours Rendered: "))
            break
        except ValueError:
            print("Hours must be a number")
            continue

    while True:
        try:
            r = float(input("Enter Employee Rate: "))
            break
        except ValueError:
            print("Rate must be a number")
            continue

    ename = Employee(n, s)

    esalary = Salary(h, r)

    gross = round(compute(h, r), 2)
    tax = round(gross * 0.1, 2)
    net = round(gross - tax, 2)
    epayroll = Payroll(gross, tax, net)

    print("="*20)
    print("EMPLOYEE RESULT  ")
    ename.show_name()
    ename.show_status()
    esalary.show_hour()
    esalary.show_hrate()
    epayroll.show_gross()
    epayroll.show_tax()
    epayroll.show_net()
    print("="*20)
    break

