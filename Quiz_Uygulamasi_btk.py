#Question
class Question:
    def __init__(self,text,choices,answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    def check(self,answer):
        return self.answer == answer

"""q1 = Question("En iyi programlama dili hqngisidir?",['C#','Python','JavaScript','Java'],'Python')
q2 = Question("En populer programlama dili hqngisidir?",['Python','JavaScript','C#','Java'],'Python')
q3 = Question("En cok kazandiran programlama dili hqngisidir?",['C#','JavaScript','Java','Python'],'Python')

print(q1.check('Python'))
print(q2.check('C#'))
print(q3.check('Java'))"""

#Quiz
class Quiz:
    def __init__(self,questions):
        self.questions = questions
        self.score = 0
        self.questionIndex = 0 #1 yazarsak diger soru karsimiza gelir.

    def getQuestion(self):
        return self.questions[self.questionIndex]

    #Kullaniciya Question'u Gostermek
    def displayQuestion(self):
        question = self.getQuestion()
        print(f"Soru {self.questionIndex +1}: {question.text}")

        for q in question.choices:
            print('- '+ q)

        answer = input("Cevabi Girin: ")
        self.guess(answer)
        self.loadQuestion()

    def guess(self,answer):
        question = self.getQuestion()

        if question.check(answer):
            self.score+=1
        self.questionIndex+=1

        #self.displayQuestion() #Soru sayisi asildiginda hata verir.

    def loadQuestion(self):
        if len(self.questions) == self.questionIndex:
            self.showScore()
        else:
            self.displayProgress()
            self.displayQuestion()

    def showScore(self):
        print('Score: ',self.score)

    def displayProgress(self):
        totalQuestion = len(self.questions)
        questionNumber = self.questionIndex +1

        if questionNumber > totalQuestion:
            print("Quiz Bitti.")
        else:
            print(f'Question: {questionNumber} of {totalQuestion}'.center(100,'*'))

q1 = Question("En iyi programlama dili hqngisidir?",['C#','Python','JavaScript','Java'],'Python')
q2 = Question("En populer programlama dili hqngisidir?",['Python','JavaScript','C#','Java'],'Python')
q3 = Question("En cok kazandiran programlama dili hqngisidir?",['C#','JavaScript','Java','Python'],'Python')

questions = [q1,q2,q3]
quiz = Quiz(questions)

"""question = quiz.getQuestion()
print(question.text)"""

"""question = quiz.questions[quiz.questionIndex]
print(question.text)"""

quiz.loadQuestion()
