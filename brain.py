class Brain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def is_input_right(self, user_input):
        return user_input.lower() == 'true' or user_input.lower() == 'false'

    def is_empty(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current.text} (True/False): ")
        if self.is_input_right(user_answer):
            self.check_answer(user_answer, current.answer)
        else:
            print("Type just true or false in correct way!")

    def check_answer(self, user_answer, current_answer):
        if user_answer.lower() == current_answer.lower():
            self.score += 1
            print("Congrats. It's True.")
        else:
            print(f"Sorry. It's wrong.")
        print(f"Your score is: {self.score}/{self.question_number}")
        print("\n")
