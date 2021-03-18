from question_model import Question
from Data import question_data
from quiz_brain import QuizBrain


question_bank = []
for question in range(1, 13):
    question = Question(question_data[question - 1]['text'], question_data[question - 1]['answer'])
    question_bank.append(question)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz.")
print(f"You're final score was: {quiz.score}/{quiz.question_number}")
