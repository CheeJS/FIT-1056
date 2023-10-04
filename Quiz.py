class Quiz:
    def __init__(self,topic,question,choices,answer,quiz_data) -> None:
        self.topic =topic
        self.question = question
        self.choices = choices
        self.answer = answer
        self.full_grade = len(quiz_data)


