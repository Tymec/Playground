import sqlite3
import os

database_name = "school.sqlite"

class Project:
    def __init__(self, database_name):
        self.db, self.cursor = self.establish_connection(database_name)

    @staticmethod
    def establish_connection(db_name):
        conn = sqlite3.connect(db_name)
        c = conn.cursor()
        c.execute("PRAGMA foreign_keys = 1")
        return conn, c
        
    def add(self, table_name, params):
        values = []
        for param in params:
            val = input(f"Enter {param}: ")
            values.append(f"'{val}'")
        
        self.cursor.execute(f"INSERT INTO {table_name} ({','.join(params)}) VALUES ({','.join(values)})")
        return f"Added {table_name[:-1]} with id {self.cursor.lastrowid}."
        
    def remove(self, table_name, param, id):
        if self.count(table_name, param, id) == 0:
            return "No value {param} with id {id} in {table_name}"
        
        self.cursor.execute(f"DELETE from {table_name} where {param} = {id}")
        self.db.commit()
        return f"Removed {table_name[:-1]} with id {id}."
    
    def count(self, table, param, value):
        self.cursor.execute(f"SELECT count(*) FROM {table} WHERE {param} = {value}")
        data = self.cursor.fetchone()[0]
        return data
        
    def count_and(self, table, val_dict):
        and_string = ""
        for key, value in val_dict.items():
            and_string += f"{key} = {value}"
            and_string += " AND "
            
        self.cursor.execute(f"SELECT count(*) FROM {table} WHERE {and_string.rstrip('AND ')}")
        data = self.cursor.fetchone()[0]
        return data
    
    def add_st(self):
        table_name = "student_course"
        params = ['student_id', 'course_id']
        
        values = []
        for param in params:
            val = input(f"Enter {param}: ")
            values.append(f"'{val}'")
        
        if self.count("students", "id", values[0]) == 0:
            return f"There is no student with id {values[0]}"
        if self.count("courses", "id", values[1]) == 0:
            return f"There is no course with id {values[1]}"
            
        self.cursor.execute(f"SELECT max_students FROM courses WHERE id = {values[1]}")
        max_students = self.cursor.fetchone()[0]
        current_students = self.count("student_course", "course_id", values[1])
        if current_students >= max_students:
            return "Max students reached"
        if self.count_and("student_course", {"student_id": values[0], "course_id": values[1]}) != 0:
            return "Student already in course"
       
        self.cursor.execute(f"INSERT INTO {table_name} ({','.join(params)}) VALUES ({','.join(values)})")
        return f"Added student {values[0]} to course {values[1]}."
    
    def list_courses(self):
        student_id = input(f"Enter student_id: ")
        
        if self.count("students", "id", student_id) == 0:
            return f"There is no student with id {student_id}"
        
        self.cursor.execute(f"SELECT course_id FROM student_course WHERE student_id = {student_id}")
        courses = self.cursor.fetchall()

        msg = "Courses:\n"
        for course_id in courses:
            self.cursor.execute(f"SELECT name FROM courses WHERE id = {course_id[0]}")
            course_name = self.cursor.fetchone()
            msg += f"\tCourse: {course_name[0]}\n"
        return msg
    
    def list_tests(self):
        course_id = input(f"Enter course_id: ")
        
        if self.count("courses", "id", course_id) == 0:
            return f"There is no course with id {course_id}"
        
        self.cursor.execute(f"SELECT name FROM tests WHERE course_id = {course_id}")
        tests = self.cursor.fetchall()
        
        msg = "Tests:\n"
        for test in tests:
            msg += f"\tTest: {test[0]}\n"
        return msg
    
    def menu(self):
        action_msg = "Welcome!"
        msg = (
            "\n"
            "1) Add student \n"
            "2) Add course \n"
            "3) Add test \n"
            "4) Add student to course \n"
            "5) List courses by student \n"
            "6) List tests by course \n"
            "7) Exit"
        )
        while 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            
            print(action_msg)
            print(msg)
            choice = input("Enter: ")
            
            if choice == '1':
                params = ['name', 'email', 'year']
                action_msg = self.add("students", params)
            elif choice == '2':
                params = ['name', 'max_students']
                action_msg = self.add("courses", params)
            elif choice == '3':
                params = ['course_id', 'name', 'date_time']
                action_msg = self.add("tests", params)
            elif choice == '4':
                action_msg = self.add_st()
            elif choice == '5':
                action_msg = self.list_courses()
            elif choice == '6':
                action_msg = self.list_tests()
            elif choice == '7':
                break
            else:
                action_msg = "Invalid choice"
            self.save()
        return
        
    def save(self):
        self.db.commit()
        
    def close(self):
        if self.cursor():
            self.cursor.close()
        if self.db:
            self.db.close()
        
if __name__ == "__main__":
    project = Project(database_name)
    project.menu()
    