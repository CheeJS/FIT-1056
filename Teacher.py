from User import User
from Quiz import Quiz
from Learner import Learner

class Teacher(User):
    def __init__(self, fName, lName, username, password):
        super().__init__(fName, lName, username, password, "Teacher")

    def view_student_progress(self, learners,all_quizzes):
        print("Student Progress:")
        for learner in learners:
            print(f"{learner.firstname}'s Grades:")
            for quiz, score in learner.quiz_attempts.items():
                print(f"- Quiz: {quiz}, Score: {score}")
            not_attempted_quizzes = self.find_not_attempted_quizzes(learner, all_quizzes)
            if not_attempted_quizzes:
                print(f"{learner.firstname} has not attempted the following quizzes:")
                for quiz in not_attempted_quizzes:
                    print(f"- {quiz}")

    def find_not_attempted_quizzes(self, learner, all_quizzes):
        attempted_quizzes = learner.quiz_attempts.keys()
        not_attempted_quizzes = [quiz.title for quiz in all_quizzes if quiz.title not in attempted_quizzes]
        return not_attempted_quizzes

if __name__ == "__main__":
    # Create some quizzes
    all_quizzes = [
        Quiz(101, "Python Basics Quiz", ["Question 1", "Question 2"]),
        Quiz(102, "JavaScript Fundamentals Quiz", ["Question 1", "Question 2"]),
        Quiz(103, "HTML Basics Quiz", ["Question 1", "Question 2"])
    ]

    # Create some learners
    learner1 = Learner("Alice", "Smith", "alice123", "password123")
    learner2 = Learner("Bob", "Johnson", "bob456", "password456")

    # Simulate learners attempting quizzes
    learner1.attempt_quiz(all_quizzes[0], 90)
    learner1.attempt_quiz(all_quizzes[1], 88)
    learner2.attempt_quiz(all_quizzes[1], 92)

    # Create a teacher
    teacher = Teacher("Teacher", "Smith", "teacher1", "teacherpass")

    # Call the view_student_progress method to view learner progress
    teacher.view_student_progress([learner1, learner2], all_quizzes)
