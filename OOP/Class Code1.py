
class person:
    def __init__(self):
        self.name = "Aniket"
        self.age = 21
    def get_info(self):
        print("Name: " + self.name + ". " + "Age " + str(self.age))
    def update(self):
        self.age = 23
    def update(self, new_age):
        self.age = new_age    
    def compare(self, other):
        if self.age > other.age:
            print(self.name + " is elder than " + other.name)
        elif self.age < other.age:
            print(other.name + " is elder than " + self.name)
        elif self.age == other.age:
            print(self.name + " is same with " + other.name)


P1 = person()
P2 = person()

print(P1.name)
P2.name = "Satya"
P2.age = 12
# P1.get_info()
# P2.get_info()
# P2.update()
# P2.get_info()
P2.update(21)
P2.compare(P1)