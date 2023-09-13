from Admin import Admin
from Learner import Learner
from Quiz import Quiz
from Lesson import Lesson
from Teacher import Teacher

def main():
    # Create users
    learner1 = Learner("Alice", "Smith", "alice123", "password123")
    learner2 = Learner("Bob", "Johnson", "bob456", "password456")

    teacher1 = Teacher("Jake", "Blake", "jake789", "password789")

    admin1 = Admin("Admin", "Admin", "admin1", "adminpass")


    # Create lessons and quizzes
    lesson1 = Lesson(1, "Python Basics", "This is a lesson about Python basics.")
    lesson2 = Lesson(2, "JavaScript Fundamentals", "This is a lesson about JavaScript fundamentals.")
    all_quizzes = [
        Quiz(101, "Python Basics Quiz", ["Question 1", "Question 2"]),
        Quiz(102, "JavaScript Fundamentals Quiz", ["Question 1", "Question 2"]),
        Quiz(103, "HTML Basics Quiz", ["Question 1", "Question 2"])
    ]

    print()
    
    # Users view lessons
    learner1.view_lesson(lesson1)
    learner2.view_lesson(lesson2 )
    print()

    # Users attempt quizzes
    learner1.attempt_quiz(all_quizzes[0], 90)
    learner1.attempt_quiz(all_quizzes[1], 88)
    learner1.view_all_grades()
    print()
    
    #Teacher view student progress
    teacher1.view_student_progress([learner1,learner2], all_quizzes)
    print()
    
    #Admin view students and teachers NAME
    admin1.view_students([learner1,learner2])
    admin1.view_teachers([teacher1])
    print()
    
    # Print user types
    print(f"{learner1.firstname}'s user type: {learner1.role}")
    print(f"{learner2.firstname}'s user type: {learner2.role}")
    print(f"{teacher1.firstname}'s user type: {teacher1.role}")
    print(f"{admin1.firstname}'s user type: {admin1.role}")
    print()


if __name__ == "__main__":
    main()