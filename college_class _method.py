# Create class College with class method display_college that prints college name

class College:
    college= 'ABC College'

    @classmethod
    def display_college(cls):
        print(f'College: {cls.college}')

College.display_college()
