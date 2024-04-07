import connection_handler
import sqlite3

class DataGen():
    def __init__(self):
         self.connector = connection_handler.SQLConnector()
         #self.connection = self.connector.get_connection()
         self.cursor = self.connector.get_cursor()

    def insert_data(self):
        try:
            x = self.cursor.execute('INSERT INTO students (name) VALUES (?)', ('Djohn Doe',))
            self.connector.connection.commit()
            print(x.rowcount)
            self.connector.close_connection()
            print("ok")
        except Exception as e:
            print(e)


if __name__ == "__main__":
    db = DataGen()
    db.insert_data()
    #  con = sqlite3.connect('database.db')
    #  cursor = con.cursor()
    #  cursor.execute('INSERT INTO students (name) VALUES (?)', ('Djohn Doe',))
    #  con.commit()
    #  con.close()

    """
    --1
SELECT s.name, AVG(grades.grade) as avg_grade
FROM students AS s
INNER JOIN grades AS grades ON s.id = grades.student_id
GROUP BY s.id
ORDER BY avg_grade DESC
LIMIT 5;
--2
SELECT s.name, AVG(grades.grade) as avg_grade
FROM students AS s
INNER JOIN grades AS grades ON s.id = grades.student_id
INNER JOIN subjects AS subj ON grades.subject_id = subj.id
WHERE subj.subj_name = :subject_name
GROUP BY s.id
ORDER BY avg_grade DESC
LIMIT 1;
--3
SELECT grp.group_name, AVG(grades.grade) as avg_grade
FROM students AS s
INNER JOIN grades AS grades ON s.id = grades.student_id
INNER JOIN subjects AS subj ON grades.subject_id = subj.id
INNER JOIN groups as grp on s.group_id = grp.id 
WHERE subj.subj_name = :subject_name
GROUP BY grp.id;
--4
SELECT AVG(grd.grade) from grades grd;
--5
SELECT sbj.subj_name FROM teachers t INNER JOIN subjects sbj on t.id =sbj.teacher_id WHERE t.teacher_name  = :teacher_name GROUP BY sbj.subj_name; 
--6
SELECT s.name from students s INNER JOIN groups grp on s.group_id = grp.id WHERE grp.group_name = :groupName;
--7
SELECT std.name , g.grade, g.date  from grades g  INNER JOIN  students std  on g.student_id  = std.id INNER JOIN groups grp ON std.group_id = grp.id INNER JOIN subjects sbj ON g.subject_id =sbj.id  WHERE (grp.group_name = :g_name) AND (sbj.subj_name = :sbj_n)

SELECT *  from subjects s ;



    
    """
