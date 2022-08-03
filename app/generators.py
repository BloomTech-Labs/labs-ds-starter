""" Random Data Generators """
from random import normalvariate
from math import ceil

from app.utilities import percent_true, clamp
from app.utilities import random_name, random_email
from app.validation import User


class RandomUser:
    """ Random User Generator Class

    DocTests - Asserts 1000 RandomUser() are valid Users()
    >>> assert all(User(**vars(RandomUser())) for _ in range(1000))
    """

    def __init__(self):
        """ Creates a Random User """
        self.name = random_name(percent_male=66)
        self.age = clamp(ceil(normalvariate(24, 5)), 1, 120)
        self.email = random_email(self.name)
        self.active = percent_true(43)
        self.score = clamp(normalvariate(0.5, 0.03125), 0.0, 1.0)
