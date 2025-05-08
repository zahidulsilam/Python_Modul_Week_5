class school :
    def __init__(self, name, foundation_year):
        self.name = name
        self.foundation_year = foundation_year
        self.students = []
        self.teachers = []

    def add_new_student(self, student_name, student_class):
        self.students.append({"name" : student_name , "class" : student_class})

    def add_new_teacher (self ,teatcher_name , branch):
        self.teachers.append ({'name' : teatcher_name,"branch":branch})
        
    def view_student_list(self):
        print("students_list: ")
        for student in self.students :
                print (f"Student Name:{student['name']}, Student Class : {student['class']}")

    def view_teacher_list(self):
        print("Teacher List:")
        for teacher in self.teachers:
            print(f"Teacher Name: {teacher['name']}, Teacher Branch: {teacher['branch']}")
    
