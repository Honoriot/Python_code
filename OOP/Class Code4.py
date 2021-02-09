
class transport:
    def __init__(self, People_sit):
        self.People_sit = People_sit
    
    def Num_Of_People(self):
        print("People travels " + str(self.People_sit))

    @staticmethod
    def Dur_Of_Travel(value):
        print("Travelling for " + str(value) + " time.")

class automobile:
    def __init__(self, Wheel):
        self.Wheel = Wheel
    
    def Number_Of_Wheel(self):
        print("Has " + str(self.Wheel) + " wheels")

class car(transport, automobile):
    def __init__(self, milage, People_sit, Wheel):
        self.milage = milage
        super().__init__(People_sit)
        #self.People_sit = People_sit
        self.Wheel = Wheel
    def Milage(self):
        print("Milage given: " + str(self.milage))

class truck(car):
    def __init__(self, load, milage, People_sit, Wheel):
        self.load = load
        self.milage = milage
        self.People_sit = People_sit
        self.Wheel = Wheel
    def Load(self):
        print("Load Carry: " + str(self.load))


truck1 = car(23, 3, 6)
truck2 = truck(4500, 1000, 2, 12)
truck1.Num_Of_People()
truck1.Dur_Of_Travel(34)
truck2.Load()
truck2.Dur_Of_Travel(300)
Aero = transport(250)
Aero.Num_Of_People()
Aero.Dur_Of_Travel(2)