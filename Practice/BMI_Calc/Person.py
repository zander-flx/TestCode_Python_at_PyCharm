class Person:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def show_name(self):
        print("Name:",self.name)