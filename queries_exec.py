import connection_handler
import re

# Dictionary to map query numbers to file names
query_files = {i: f"query_{i}.sql" for i in range(1, 11)}
tasks = {
    1: "Find the 5 students with the highest GPA(grate point average) across all subjects.",
    2: "Find the student with the highest GPA in a particular subject.",
    3: "Find the average score in groups for a certain subject.",
    4: "Find the average score on the stream (across the entire scoreboard grades table).",
    5: "Find what courses a particular teacher teaches.",
    6: " Find a list of students in a specific group.",
    7: "Find the grades of students in a separate group for a specific subject.",
    8: "Find the average score given by a certain teacher in his subjects.",
    9: "Find a list of courses a student is taking.",
    10: "A list of courses taught to a specific student by a specific instructor."

}

def get_user_input(query_number):
    parameters = {}
    print(tasks[query_number])
    if query_number in [2, 3]:        
        user_input = input(f"Enter parameter value for <subject name> ({query_number}): ")
        parameters['subject_name'] = user_input
    elif query_number in [5, 8]:
        user_input = input(f"Enter parameter value for <teacher name> ({query_number}): ")
        parameters['teacher_name'] = user_input
    elif query_number in [6]:
        user_input = input(f"Enter parameter value for <group name> ({query_number}): ")
        parameters['group_name'] = user_input
    elif  query_number in [7]:
        user_input = input(f"Enter parameter value for <group name> ({query_number}): ")
        parameters['group_name'] = user_input
        user_input = input(f"Enter parameter value for <subject name> ({query_number}): ")
        parameters['subject_name'] = user_input
    elif  query_number in [10]:
        user_input = input(f"Enter parameter value for <student name> ({query_number}): ")
        parameters['student_name'] = user_input
        user_input = input(f"Enter parameter value for <teacher name> ({query_number}): ")
        parameters['teacher_name'] = user_input  
    elif query_number == 9:  
        user_input = input(f"Enter parameter value for <student name> ({query_number}): ")
        parameters['student_name'] = user_input
    return parameters

def execute_query(query_number, parameters, conn):
    if query_number == 0:
         return    
    filename = query_files.get(query_number)
    file_path = f"./HW6_resulting_queries/{filename}"
    
    
    with open(file_path, 'r') as file:
        query = file.read()

    # Replace SQL variables with ?
    pattern = r":[a-zA-Z]+_name"
    query = re.sub(pattern, "?", query)
    
    # Connect to SQLite database        
    cursor = conn.get_cursor()  
    results = None  

    try:
        if query_number in [2, 3]:
                cursor.execute(query, (parameters['subject_name'],))
        elif query_number in [5, 8]:
                cursor.execute(query, (parameters['teacher_name'],))
        elif query_number == 6:
                cursor.execute(query, (parameters['group_name'],))
        elif query_number == 7:
                cursor.execute(query, (parameters['group_name'],parameters['subject_name']))
        elif query_number== 10:
                cursor.execute(query, (parameters['student_name'], parameters['teacher_name']))
        elif query_number in [1, 4]:
                cursor.execute(query)
        elif query_number == 0:
                conn.close_connection()
        elif query_number == 9:
            cursor.execute(query, (parameters['student_name'], ))
        results = cursor.fetchall()
        for row in results:
            print(row)

    except Exception as e:
        print(f"Error executing query: {e}")
    
def main():
    conn = None
    try:
        conn = connection_handler.SQLConnector()
        while True:
            print("Enter the query number (1-10) to execute (or 0 to exit): ")
            try:
                query_number = int(input())
                if query_number == 0:
                    parameters = {}
                    execute_query(query_number, parameters, conn)
                    break
                elif query_number in range(1, 11):
                    parameters = get_user_input(query_number)
                    execute_query(query_number, parameters, conn)
                else:
                    print("Invalid input. Please enter a number between 1 and 10.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    finally:
         if conn:
              conn.close_connection()

if __name__ == "__main__":
    main()
