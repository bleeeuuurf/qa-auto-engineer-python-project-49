import secrets

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number < 2:
        return False
    divisor = 2
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 1
    return True


def get_question_and_answer():
    number = secrets.randbelow(100) + 1
    question = str(number)
    correct_answer = 'yes' if is_prime(number) else 'no'
    return question, correct_answer