
class computer:
    def __init__(self, CPU, RAM):
        #print("Call me first")
        self.CPU = CPU
        self.RAM = RAM
    def config(self):
        print(self.CPU)
        print(self.RAM)


comp1 = computer("i5", 16)
comp2 = computer("Ryzen 5 3600", 8)

computer.config(comp1)
comp2.config()
print(id(comp1))
print(id(comp2))
del comp1, comp2