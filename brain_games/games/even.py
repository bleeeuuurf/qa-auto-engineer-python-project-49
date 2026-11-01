import secrets

RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def get_question_and_answer():
    number = secrets.randbelow(100) + 1
    question = str(number)
    correct_answer = 'yes' if is_even(number) else 'no'
    return question, correct_answer