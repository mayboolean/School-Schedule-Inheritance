from school_schedule.middle_school_student import MiddleSchoolStudent

def test_new_valid_middle_school_student_gets_transportation():
    # Arrange
    name = "Ellis"
    grade = "junior"
    classes = ["Painting"]

    # Act
    ellis = MiddleSchoolStudent(name, grade, classes, gets_transportation=True)

    assert ellis.name == name
    assert ellis.grade == grade
    assert ellis.classes == classes
    assert len(ellis.classes) == 1
    assert ellis.gets_transportation

def test_new_valid_middle_school_student_with_defaults():
    name = "Ellis"
    grade = "junior"
    classes = ["Painting"]

    # Act
    ellis = MiddleSchoolStudent(name, grade, classes)
    assert ellis.name == name
    assert ellis.grade == grade
    assert ellis.classes == classes
    assert len(ellis.classes) == 1
    assert not ellis.gets_transportation


def test_middle_school_student_summary_with_transportation():
    # Arrange
    name = "Ellis"
    grade = "junior"
    classes = ["Painting"]

    # Act
    ellis = MiddleSchoolStudent(name, grade, classes, gets_transportation=True)

    assert ellis.summary() == ("Ellis is a junior "
            "enrolled in 1 class: Painting"
            "\nEllis has transportation")

def test_middle_school_student_summary_without_transportation():
    # Arrange
    name = "Ellis"
    grade = "junior"
    classes = ["Painting"]

    # Act
    ellis = MiddleSchoolStudent(name, grade, classes)

    assert ellis.summary() == ("Ellis is a junior "
            "enrolled in 1 class: Painting"
            "\nEllis does not have transportation")

def test_summary_with_one_class():
    name = "Ada"
    grade = "senior"
    classes = ["Computer Science"]

    ada = MiddleSchoolStudent(name, grade, classes)

    assert ada.summary() == ("Ada is a senior "
            "enrolled in 1 class: Computer Science"
            "\nAda does not have transportation")
