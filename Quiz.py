class Quiz:
    """
    Class definition for the Quiz class
    """
    def __init__(self,topic,question,choices,answer,quiz_data) -> None:
        """
        Constructor of Quiz object
        """
        self.topic =topic
        self.question = question
        self.choices = choices
        self.answer = answer
        self.full_grade = len(quiz_data)


