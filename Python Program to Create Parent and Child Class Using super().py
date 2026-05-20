# Create a parent class Employee with a constructor that accepts an integer emp_id.
# Create a child class Manager.
# Use super() inside the child class constructor to initialize emp_id and print it in the format:Employee ID: <id>

class Employee:
    def __init__(self, emp_id):
        self.emp_id = emp_id

class Manager(Employee):
    def __init__(self, emp_id):
        super().__init__(emp_id)
        print(f"Employee ID: {self.emp_id}")

Manager(int(input()))
