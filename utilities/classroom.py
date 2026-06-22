class Classroom:

    def __init__(self, teacher):
        self.teacher = teacher
        self.students = []

    def enroll(self, name, grade):
        self.students.append((name, int(grade)))

    def show_roster(self):

        print("The students in this class are:")

        for students in self.students:
            print(students)

    def class_average(self):

        total_grade = 0

        for student, grade in self.students:
            total_grade += grade

        avg_grade = total_grade/len(self.students)

        print(f"The average grade of all students is {avg_grade}.")

    def __str__(self):

        if self.teacher[-1] == "s":
            return f"{self.teacher}' class has {len(self.students)} students."

        else:
            return f"{self.teacher}'s class has {len(self.students)} students."
        

classroom1 = Classroom("Ms. Santiago")

classroom1.enroll("Asiyah G. Salvador", 95)
classroom1.enroll("Harry K. Potter", 45)
classroom1.enroll("Kyle A. Vanderbilt", 67)

classroom1.show_roster()

classroom1.class_average()

print(classroom1)
