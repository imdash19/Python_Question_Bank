# Create a parent class Vehicle with constructor accepting speed. 
# Create a child class Car. Use super() to initialize speed and display it.

class Vehicle:
    def __init__(self, speed):
        self.speed = speed

class Car(Vehicle):
    def __init__(self, speed):
        super().__init__(speed)
        print(self.speed)

Car(int(input()))
