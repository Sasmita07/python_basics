class Father:
    def hoobies(self):
        print("Love Cooking")

class Mother:
    def hoobies(self):
        print("Love Gardening")

class Child(Father, Mother):
    def hoobies(self):
        Father.hoobies(self)
        Mother.hoobies(self)
        print("Love Playing")

c = Child()
c.hoobies()