# HW6WEBSQL
Instructions
TBD

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

     Find the 5 students with the highest GPA(grate point average) across all subjects.
     Find the student with the highest GPA in a particular subject.
     Find the average score in groups for a certain subject.
     Find the average score on the stream (across the entire scoreboard).
     Find what courses a particular teacher teaches.
     Find a list of students in a specific group.
     Find the grades of students in a separate group for a specific subject.
     Find the average score given by a certain teacher in his subjects.
     Find a list of courses a student is taking.
     A list of courses taught to a specific student by a specific instructor.

For each request, issue a separate query_number.sql file, where instead of number, substitute the number of the request. The file contains an SQL statement that can be executed both in the database terminal and via cursor.execute(sql)

Additional task

​

For an additional task, make the following requests of increased complexity:

     The average score given by a particular teacher to a particular student.
     Grades of students in a certain group in a certain subject in the last lesson.
