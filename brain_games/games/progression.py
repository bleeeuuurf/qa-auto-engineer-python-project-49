import secrets

RULES = 'What number is missing in the progression?'
MIN_LENGTH = 5
MAX_LENGTH = 10


def generate_progression(start, step, length):
    return [start + index * step for index in range(length)]


def get_question_and_answer():
    length = secrets.randbelow(MAX_LENGTH - MIN_LENGTH + 1) + MIN_LENGTH
    start = secrets.randbelow(20) + 1
    step = secrets.randbelow(10) + 1
    progression = generate_progression(start, step, length)

    hidden_index = secrets.randbelow(length)
    correct_answer = str(progression[hidden_index])

    progression[hidden_index] = '..'
    question = ' '.join(map(str, progression))
    return question, correct_answer