# Create a class named BonusCalculator with a method calculate_bonus().
# If only salary is passed, calculate a 10% bonus.
# If salary and performance rating are passed, calculate the bonus based on the rating.

# | Rating | Bonus Percentage |
# | ------ | ---------------- |
# | A      | 20%              |
# | B      | 15%              |
# | C      | 10%              |

class BonusCalculator:
    def calculate_bonus(self, salary, rating=None):
        if rating is None:
            bonus = salary * 10 / 100
        else:
            if rating == "A":
                bonus = salary * 20 / 100
            elif rating == "B":
                bonus = salary * 15 / 100
            else:
                bonus = salary * 10 / 100

        print(f"{bonus:.2f}")

b = BonusCalculator()

n = int(input())

if n == 1:
    salary = float(input())
    b.calculate_bonus(salary)

elif n == 2:
    salary = float(input())
    rating = input()
    b.calculate_bonus(salary, rating)
