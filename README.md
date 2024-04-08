# HW6WEBSQL

Instructions and project description

1. To generate DB data it can be used populate_data.py script. It creates tables and fills them with fake data.
2. It can be changed DB type (now it's implemented MariaDB and SQLite). The DB type can be changed in config.ini file.
   Don't forget to update DB cridentials as well. In case of MariaDB database should be created manually.
3. You can run resulting queries from Home Work #6 (stored in HW6_resulting_queries folder) using any SQL client (e.g. DBeaver,DBGate...etc).
4. It is possible to run and get results for the queries using queries_exec.py script. You will need to set number of query and provide any parameters requested. To exit set 0 and hit enter key.

Sample data to use in query (present in database.db):
student = Stacy Flores
group name = Applied Mathematics
subject name = Statistics
teacher = Michael Soto

Task details:

Implement a database whose schema contains:

     Table of students;
     Table of groups;
     Table of teachers;
     Table of subjects with the indication of the teacher who reads the subject;
     A table where each student has grades in subjects with an indication of when the grade was received;

Fill the resulting database with random data (~30-50 students, 3 groups, 5-8 subjects, 3-5 teachers, up to 20 grades for each student in all subjects).

Use the Faker pack to fill the database.

Make the following selections from the obtained database:

     1. Find the 5 students with the highest GPA(grate point average) across all subjects.
     2. Find the student with the highest GPA in a particular subject.
     3. Find the average score in groups for a certain subject.
     4. Find the average score on the stream (across the entire scoreboard grades table).
     5. Find what courses a particular teacher teaches.
     6. Find a list of students in a specific group.
     7. Find the grades of students in a separate group for a specific subject.
     8. Find the average score given by a certain teacher in his subjects.
     9. Find a list of courses a student is taking.
     10. A list of courses taught to a specific student by a specific instructor.

For each request, issue a separate query_number.sql file, where instead of number, substitute the number of the request. The file contains an SQL statement that can be executed both in the database terminal and via cursor.execute(sql)

Additional task

​

For an additional task, make the following requests of increased complexity:

     1. The average score given by a particular teacher to a particular student.
     2. Grades of students in a certain group in a certain subject in the last lesson.
