from faker import Faker
import random
import connection_handler
import logger_instance

class DataGenerator():    

    def __init__(self):
        self.logger = logger_instance.HWLogging()
        self.fakegen = Faker()
        self.DB_TYPE = 'sqlite' # Can be selected 'mariadb' or 'sqlite'
        
        # Number of records in tables to generate
        self.NUMBER_OF_STUDENTS = (30, 50)                
        self.NUMBER_OF_TEACHERS = (3, 5)        
        
        # Group names and subjects        
        self.groups = {'AM-24-01' : 'Applied Mathematics', 'CS-24-01' : 'Computer Science', 'AI-24-01' : 'Computer Cybernetics and AI'}
        self.subjects = ['Mathematical Analysis', 'Descrete Mathematics', 'Matematical Modeling', 'Statistics', 'Object Oriented Programming (C++)', 'Voice Recognition', 'Coputer Graphics']
        
        # Grades
        self.GRADE_RANGE = (1, 12)

        # Create  connection
        self.connector = connection_handler.SQLConnector()        
        self.queries = self.connector.get_queries(self.DB_TYPE)
        self.cursor = self.connector.get_cursor()
    
    def create_populate_database(self):  

        create_script_names=['create_groups', 'create_students', 'create_teachers', 'create_subjects', 'create_marks']
        # Create tables
        for script_name in create_script_names:
            self.logger.log_info("script_name are applied and table is created")
            self.execute_table_create_script(self.queries[script_name])

        self.connector.connection.commit()

        # Generate random data and fill tables
        self.generate_data()

        self.connector.close_connection()

    def generate_data(self):
        
        fake = self.fakegen
        # Generate groups 
        self.logger.log_info("Generate groups")        
        groups = self.groups
        for id, group in groups.items():
            self.cursor.execute(self.queries['insert_groups'], (id, group))

        # Generate students and assign to groups
        self.logger.log_info("Generate students")
        group_ids = [row[0] for row in self.cursor.execute('SELECT id FROM groups')]
        for _ in range(random.randint(self.NUMBER_OF_STUDENTS[0], self.NUMBER_OF_STUDENTS[1])):
            group_id = random.choice(group_ids)
            self.cursor.execute(self.queries['insert_students'], (fake.name(),group_id)) 

        # Generate teachers
        self.logger.log_info("Generate teachers")
        for _ in range(random.randint(self.NUMBER_OF_TEACHERS[0], self.NUMBER_OF_TEACHERS[1])):
            self.cursor.execute(self.queries['insert_teachers'], (fake.name(),))

        # Generate subjects and assign teachers
        self.logger.log_info("Generate subjects")
        subjects = self.subjects
        teacher_ids = [row[0] for row in self.cursor.execute('SELECT id FROM teachers')]
        for subject in subjects:
            teacher_id = random.choice(teacher_ids)
            self.cursor.execute(self.queries['insert_subjects'], (subject, teacher_id))

        # Generate grades for each student in all subjects
        student_ids = [row[0] for row in self.cursor.execute('SELECT id FROM students')]
        subject_ids = [row[0] for row in self.cursor.execute('SELECT id FROM subjects')]
        for student_id in student_ids:
            for subject_id in subject_ids:
                grade = random.randint(1, 10)
                date = fake.date_between(start_date='-1y', end_date='today').strftime('%Y-%m-%d')
                self.cursor.execute(self.queries['insert_marks'],
                           (student_id, subject_id, grade, date))
        self.connector.connection.commit()
    
    def execute_table_create_script(self, query):
        self.cursor.execute(query)

if __name__ == '__main__':
   dg = DataGenerator()
   dg.create_populate_database()



    
