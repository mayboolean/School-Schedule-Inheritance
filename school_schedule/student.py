class Student:
    def __init__(self, name, grade, classes):
        self.name = name
        self.grade = grade
        self.classes = classes

    def add_class(self, class_name):
        self.classes.append(class_name)
        return self.classes

    def get_num_classes(self):
        return len(self.classes)

    def display_classes(self):
        return ", ".join(self.classes)

    def summary(self):
        class_vs_classes = "class" if len(self.classes) == 1 else "classes"
        return (f"{self.name} is a {self.grade} "
            f"enrolled in {self.get_num_classes()} {class_vs_classes}: "
            f"{self.display_classes()}")
        
        
    