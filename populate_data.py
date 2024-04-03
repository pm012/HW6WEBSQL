
from faker import Faker



class InstanceGenerator():
    NUMBER_OF_STUDENTS = 35
    NUMBER_OF_GROUPS = 3
    NUMBER_OF_SUBJECTS = 6
    NUMBER_OF_TEACHERS = 4
    NUMBER_OF_MARKS  = 20

    def __init__(self):
        self.fakegen = Faker()


    
