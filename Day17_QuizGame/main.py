from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

questionbank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    questionbank.append(new_question)

quiz = QuizBrain(questionbank)
quiz.next_question()

while quiz.still_has_questions():
    quiz.next_question()

quiz.complete()

