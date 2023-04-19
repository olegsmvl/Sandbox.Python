class Parent:
    def __init__(self):
        self.w = 1
        self.z = 2
    def get_values(self):
        return [self.w , self.z]

class Child(Parent):
    def get_first_value(self):
        return self.w

if __name__ == "__main__":
    p = Child()
    res = p.get_first_value()
    print(res)