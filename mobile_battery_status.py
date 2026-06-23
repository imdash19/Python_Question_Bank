# Create a Mobile class with a constructor.
# The constructor should accept battery percentage and print:

# "Charge Phone" if battery < 20
# "Battery OK" if battery ≥ 20

class Mobile:
    def __init__(self, battery_percentage):
        self.battery_percentage= battery_percentage

m= Mobile(int(input()))

if m.battery_percentage >= 20:
    print("Battery OK")

else:
    print("Charge Phone")
