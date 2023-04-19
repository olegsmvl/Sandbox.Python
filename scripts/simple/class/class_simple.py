class Printer:
    def do_it(self):
        pass

class Calc:
    def sum(self, a, b):
        print(a+b)

    def sum_twice(self, a, b):
        self.sum(a,b)
        self.sum(a,b)

def main():
    cl = Calc()
    cl.sum(5,10)
    cl.sum_twice(8, 2)
    pr = Printer()
    pr.do_it()


main()