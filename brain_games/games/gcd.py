import secrets

RULES = 'Find the greatest common divisor of given numbers.'


def gcd(first, second):
    while second:
        first, second = second, first % second
    return first


def get_question_and_answer():
    first = secrets.randbelow(100) + 1
    second = secrets.randbelow(100) + 1
    question = f'{first} {second}'
    correct_answer = str(gcd(first, second))
    return question, correct_answer
    