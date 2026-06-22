# Create class College with class method display_college that prints college name

class College:
    college_name = "ABC College"

    @classmethod
    def display_college(cls):
        print(cls.college_name)

College.display_college()
