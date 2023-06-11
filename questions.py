class Question:
    def __init__(self, question, right_answer):
        self.question = question
        self.right_answer = right_answer


questions = []
with open('practice_texts/questions.txt', 'r') as file:
    q = file.read().split('\n')
with open('practice_texts/answers.txt', 'r') as file:
    a = file.read().split('\n')

for i in range(len(q)):
    questions.append(Question(q[i], a[i]))
