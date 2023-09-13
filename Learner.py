from User import User
from Quiz import Quiz
from Lesson import Lesson

class Learner(User):
    def __init__(self,fName,lName,username,password):
        super().__init__(fName,lName,username,password,"Learner")
        self.quiz_attempts = {}

    def printName(self):
        print(self.firstname)

    def view_lesson(self,lesson):
        if lesson.type =="lesson":
            print(f"{self.firstname} is viewing the lesson: {lesson.title}")
        else:
            print("Invalid lesson.")


    def attempt_quiz(self, quiz, score):
        if quiz.type == "quiz":
            self.quiz_attempts[quiz.title] = score
        else:
            print("Invalid quiz.")

    def view_all_grades(self):
        if not self.quiz_attempts:
            print("No attempt")
        else:
            print(f"Grades for {self.firstname}:")
            for quiz, score in self.quiz_attempts.items():
                print(f"- Quiz: {quiz}, Score: {score}")
    def quizzes_not_attempted(self, all_quizzes):
        not_attempted = []
        for quiz in all_quizzes:
            if quiz.title not in self.quiz_attempts:
                not_attempted.append(quiz.title)
        return not_attempted
if __name__ == "__main__":
    # Create a Learner object
    learner1 = Learner("Alice", "Smith", "alice123", "password123")
    learner2 = Learner("James", "Smith", "alice123", "password123")


    # Create some lessons
    lesson1 = Lesson(201, "Python Variables", "This is a lesson about Python variables.")
    lesson2 = Lesson(202, "JavaScript Functions", "This is a lesson about JavaScript functions.")
    quiz1 = Quiz(101, "Python Basics Quiz", ["Question 1", "Question 2"])
    quiz2 = Quiz(102, "JavaScript Fundamentals Quiz", ["Question 1", "Question 2"])
    quiz3 = Quiz(103, "HTML Basics Quiz", ["Question 1", "Question 2"])



    # Test viewing lessons
    learner1.view_lesson(lesson1)  # Valid lesson
    learner1.view_lesson(lesson2)  # Valid lesson
   
    
    # Test attempting quizzes
    learner1.attempt_quiz(quiz1, 90)
    learner1.attempt_quiz(quiz2, 88)
    learner1.view_all_grades()
    all_quizzes = [quiz1, quiz2, quiz3]
    not_attempted_quizzes = learner1.quizzes_not_attempted(all_quizzes)
    
    
    print(f"{learner1.firstname} has not attempted the following quizzes:")
    for quiz in not_attempted_quizzes:
        print(f"- {quiz}")


    

