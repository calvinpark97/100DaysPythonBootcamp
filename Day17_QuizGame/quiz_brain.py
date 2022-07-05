class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.questions_correct = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {self.current_question.text} (True/False)")
        self.check_answer(answer)

    def check_answer(self,answer):
        if answer.lower() == self.current_question.answer.lower():
            self.questions_correct += 1
            print("You got it right!")
            print(f"The answer is {self.current_question.answer}")
            print(f"Your score is {self.questions_correct}/{(self.question_number)}")
        else:
            print("You got it wrong")
            print(f"The answer is {self.current_question.answer}")
            print(f"Your score is {self.questions_correct}/{(self.question_number)}")

    def complete(self):
        print("You have completed the quiz.")
        print(f"Your score was {self.questions_correct}/{len(self.question_list)}.")
