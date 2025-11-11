class NotEvenNumberException(Exception):
    def __init__(self, *args):
        super().__init__(*args)


def checkIsOddNumber(number):
    if number % 2 == 0:
        raise NotEvenNumberException(f"{number} is not even number.")


try:
    checkIsOddNumber(2)
except NotEvenNumberException as e:
    print(f'caught not even number exception: {e.args}')