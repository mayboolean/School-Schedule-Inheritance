from .student import Student

# add MiddleSchoolStudent here
class MiddleSchoolStudent(Student):
    def __init__(self, name, grade, classes, gets_transportation=False):
        super().__init__(name, grade, classes)
        self.gets_transportation = gets_transportation

    def summary(self):
        student_summary = super().summary()
        if self.gets_transportation:
            transportation_msg = f"{self.name} has transportation"
        else:
            transportation_msg = f"{self.name} does not have transportation"
        return "\n".join([student_summary, transportation_msg])
