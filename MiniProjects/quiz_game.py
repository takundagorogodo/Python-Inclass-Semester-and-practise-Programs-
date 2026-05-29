print("""
*****************************************
    Welcome to My Quiz Game
*****************************************
""")

import question_bank
import answers

score = 0

def check_answer(user_guess, correct_answer):
    return user_guess == correct_answer

for question_number in range(len(question_bank.questions)):
    print("*******************************")
    print(question_bank.questions[question_number]["text"])

    for option in answers.options[question_number]:
        print(option)

    guess = input("Enter your answer (A/B/C/D): ").upper()
    is_correct = check_answer(guess, question_bank.questions[question_number]["answer"])

    if is_correct:
        print("Correct Answer")
        score += 1
    else:
        print("Incorrect Answer")
        print(f"The correct answer is {question_bank.questions[question_number]['answer']}")

    print(f"Your current score is {score}/{question_number + 1}")

print(f"You answered {score} questions correctly.")

percentage = (score / len(question_bank.questions)) * 100
print(f"Your score is {percentage:.2f}%")
