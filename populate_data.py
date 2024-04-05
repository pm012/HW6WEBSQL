

from faker import Faker
import random
import os
import connection_handler
import logger_instatnce



class DataGenerator():
    

    def __init__(self):
        logger = logger_instatnce.HWLogging().get_logger() 
        self.fakegen = Faker()
        self.DB_TYPE = 'sqlite' # Can be selected 'mariadb' or 'sqlite'
        
        # Number of records in tables to generate
        self.NUMBER_OF_STUDENTS = (30, 50)        
        #self.NUMBER_OF_SUBJECTS = 6
        self.NUMBER_OF_TEACHERS = (3, 5)        
        
        # Group names and subjects        
        self.groups = {'AM-24-01' : 'Applied Mathematics', 'CS-24-01' : 'Computer Science', 'AI-24-01' : 'Computer Cybernetics and AI'}
        self.subjects = subjects = ['Mathematical Analysis', 'Descrete Mathematics', 'Matematical Modeling', 'Statistics', 'Object Oriented Programming (C++)', 'Voice Recognition', 'Coputer Graphics']
        
        # Grades
        self.GRADE_RANGE = (1, 12)
    

    def create_database(self, config_file):
    

        # Create  connection
        connection = connection_handler.SQLConnector(self.DB_TYPE)
        cursor = connection.cursor()

        # Create tables
        cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                        id INTEGER PRIMARY KEY,
                        name TEXT
                    )''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS groups (
                        id INTEGER PRIMARY KEY,
                        group_code TEXT,
                        group_name TEXT
                    )''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS teachers (
                        id INTEGER PRIMARY KEY,
                        teacher_name TEXT
                    )''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS subjects (
                        id INTEGER PRIMARY KEY,
                        subj_name TEXT,
                        teacher_id INTEGER,
                        FOREIGN KEY (teacher_id) REFERENCES teachers(id)
                    )''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS grades (
                        id INTEGER PRIMARY KEY,
                        student_id INTEGER,
                        subject_id INTEGER,
                        grade INTEGER,
                        date TEXT,
                        FOREIGN KEY (student_id) REFERENCES students(id),
                        FOREIGN KEY (subject_id) REFERENCES subjects(id)
                    )''')

        connection.commit()

        # Generate random data and fill tables
        self.generate_data(cursor)

        connection.close()

    def generate_data(self, cursor):
        
        fake = self.fakegen
        # Generate students
        for _ in range(random.randint(30, 50)):
            cursor.execute('INSERT INTO students (name) VALUES (?)', (fake.name(),))

        # Generate groups
        groups = self.groups
        for group in groups:
            cursor.execute('INSERT INTO groups (group_name, group_code) VALUES (?, ?)', (group,))

        # Generate teachers
        for _ in range(random.randint(3, 5)):
            cursor.execute('INSERT INTO teachers (teacher_name) VALUES (?)', (fake.name(),))

        # Generate subjects and assign teachers
        subjects = ['Mathematics', 'Physics', 'Chemistry', 'Biology', 'History', 'Literature', 'Art']
        teacher_ids = [row[0] for row in cursor.execute('SELECT id FROM teachers')]
        for subject in subjects:
            teacher_id = random.choice(teacher_ids)
            cursor.execute('INSERT INTO subjects (subj_name, teacher_id) VALUES (?, ?)', (subject, teacher_id))

        # Generate grades for each student in all subjects
        student_ids = [row[0] for row in cursor.execute('SELECT id FROM students')]
        subject_ids = [row[0] for row in cursor.execute('SELECT id FROM subjects')]
        for student_id in student_ids:
            for subject_id in subject_ids:
                grade = random.randint(1, 10)
                date = fake.date_between(start_date='-1y', end_date='today')
                cursor.execute('INSERT INTO grades (student_id, subject_id, grade, date) VALUES (?, ?, ?, ?)',
                           (student_id, subject_id, grade, date))

if __name__ == '__main__':
   pass



    
