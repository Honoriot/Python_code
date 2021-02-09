
class Car:
    Number_Of_Wheel = 4   # class variable
    def __init__(self):
        self.Number_Of_Seats = 4
        self.milage = 10
        self.Company = "Tata"


Altroz = Car()
Lemo = Car()

print(Altroz.Number_Of_Seats, Altroz.Number_Of_Wheel)
print(Lemo.Number_Of_Seats, Lemo.Number_Of_Wheel)

Lemo.Number_Of_Wheel = 6


print(Altroz.Number_Of_Seats, Altroz.Number_Of_Wheel)
print(Lemo.Number_Of_Seats, Lemo.Number_Of_Wheel)