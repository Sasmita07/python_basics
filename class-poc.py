class Human:
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation
    
    def do_work(self):
        if self.occupation == 'a':
            print(self.name, "do work a")
        if self.occupation == 'b':
            print(self.name, "do work b")
    
    def do_payment(self):
        if self.occupation == 'a':
            print(self.name, "payment is 1000")
        if self.occupation == 'b':
            print(self.name, "payment is 2000")

bob = Human("Bob", "a")
bob.do_work()
bob.do_payment()

tom = Human("Tom", "b")
tom.do_work()
tom.do_payment()