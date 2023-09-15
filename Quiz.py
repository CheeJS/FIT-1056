
class Quiz:
    def __init__(self, quiz_id, title, questions,answer=0):
        self.quiz_id = quiz_id
        self.title = title
        self.questions = questions
        self.grades = {}  # Dictionary to store quiz grades
        self.type = "quiz"
        self.answer = answer
