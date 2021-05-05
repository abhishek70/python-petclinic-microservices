import datetime
import random
import string


def random_lower_string() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=32))


def random_datetime() -> datetime:
    return datetime.datetime.now()


def random_integer() -> int:
    return random.randint(1, 1000)
