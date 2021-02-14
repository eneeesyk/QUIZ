from data import question_data
from question_model import Question
from brain import Brain

question_bank = []

for question in question_data:
   question_bank.append(Question(question["question"], question["correct_answer"]))

quiz = Brain(question_bank)

while quiz.is_empty():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
