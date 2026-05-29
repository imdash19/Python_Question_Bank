# Create a class named FareCalculator with a method calculate_fare().
# If only distance is passed, calculate the normal travel fare.
# If distance and passenger type are passed, apply a student discount.

# Fare Rules
# Fare per unit distance = 10
# Student discount = 20% on the total fare

class FareCalculator:
    def calculate_fare(self, distance, passenger_type=None):
        fare = distance * 10

        if passenger_type is None:
            print(fare)
        else:
            print(fare - (fare * 20 // 100))

f = FareCalculator()

n = int(input())

if n == 1:
    distance = int(input())
    f.calculate_fare(distance)

elif n == 2:
    distance = int(input())
    passenger_type = input()
    f.calculate_fare(distance, passenger_type)
