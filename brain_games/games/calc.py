import secrets

RULES = 'What is the result of the expression?'


def calculate(first, second, operator):
    match operator:
        case '+':
            return first + second
        case '-':
            return first - second
        case '*':
            return first * second


def get_question_and_answer():
    first = secrets.randbelow(100) + 1
    second = secrets.randbelow(100) + 1
    operator = secrets.choice(['+', '-', '*'])
    question = f'{first} {operator} {second}'
    correct_answer = str(calculate(first, second, operator))
    return question, correct_answer