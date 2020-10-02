from json import JSONEncoder
from quizc.model.json_quiz import JsonQuiz


class MyEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__



class QuizPersistence(object):

    @staticmethod
    def saveQuiz(title, questions, answers):
        for answer in answers.answers:
            answers = answer.answers
            
        all_questions = []

        for question in questions:
            all_questions.append(question.title)

        my_quiz = JsonQuiz(title, all_questions, answers)

        json = MyEncoder().encode(my_quiz)
        f = open("quizc/files/myform.json", "w")
        f.write(json)
        f.close()


