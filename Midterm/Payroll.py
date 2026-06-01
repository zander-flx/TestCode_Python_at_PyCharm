class Payroll:
    def __init__(self, gross, tax, net):
        self.gross = gross
        self.tax = tax
        self.net = net

    def show_gross(self):
        print("Employee Gross:", self.gross)

    def show_tax(self):
        print("Employee Tax:", self.tax)

    def show_net(self):
        print("Employee Net:", self.net)