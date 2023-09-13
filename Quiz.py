
class Quiz:
    def __init__(self, quiz_id, title, questions):
        self.quiz_id = quiz_id
        self.title = title
        self.questions = questions
        self.grades = {}  # Dictionary to store quiz grades
        self.type = "quiz"
