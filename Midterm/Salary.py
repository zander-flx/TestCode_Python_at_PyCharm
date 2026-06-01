class Salary:
    def __init__(self, hours, hrate):
        self.hour = hours
        self.hrate = hrate

    def get_hour(self):
        return self.hour

    def show_hour(self):
        print("Employee Hours:", self.hour)

    def get_hrate(self):
        return self.hrate

    def show_hrate(self):
        print("Employee Rate(per hour):", self.hrate)