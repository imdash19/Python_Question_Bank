# Create a class TreatmentCost with method get_cost(). 
# Create another class Insurance with method apply_insurance(). 
# Create a child class HospitalBill that deducts insurance amount if cost exceeds 5000.

class TreatmentCost:
    def get_cost(self):
        self.cost = int(input())

class Insurance:
    def apply_insurance(self):
        if self.cost > 5000:
            print(self.cost - 2000)
        else:
            print(self.cost)

class HospitalBill(TreatmentCost, Insurance):
    pass

h = HospitalBill()
h.get_cost()
h.apply_insurance()
