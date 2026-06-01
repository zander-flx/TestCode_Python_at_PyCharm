class Employee:
    def __init__(self, name, status):
        self.name = name
        self.status = status

    def show_name(self):
        print("Employee Name:",self.name)

    def show_status(self):
        print("Employee Status:",self.status)