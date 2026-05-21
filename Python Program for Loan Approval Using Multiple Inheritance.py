#Create a class Income with method get_income(). 
#Create another class CreditScore with method get_score(). 
#Create a child class LoanApproval that approves loan if income > 30000 and credit score > 700.

class Income:
    def get_income(self):
        self.income = int(input())

class CreditScore:
    def get_score(self):
        self.score = int(input())

class LoanApproval(Income, CreditScore):
    def approve_loan(self):
        if self.income > 30000 and self.score > 700:
            print("Loan Approved")
        else:
            print("Loan Rejected")

l = LoanApproval()
l.get_income()
l.get_score()
l.approve_loan()
