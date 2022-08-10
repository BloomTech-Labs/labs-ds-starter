""" General Utilities """
from typing import Union
from random import randint, choice

male_first_names = [
    'Brycen', 'Cash', 'Deandre', 'Kase', 'Lochlan', 'Ramon', 'Darian', 'Shiloh',
    'Keith', 'Finnley', 'Kellan', 'Erik', 'Lance', 'Jadiel', 'Ray', 'Izaiah',
    'Dennis', 'Aries', 'Leo', 'Elliot', 'Jorge', 'Edwin', 'Phillip', 'Richard',
    'Benjamin', 'Tucker', 'Pierce', 'Dax', 'Kameron', 'George', 'Kiaan',
    'Camilo', 'Kody', 'Colin', 'Alberto', 'Finley', 'Kamden', 'Ace', 'Zyair',
    'Byron', 'Rory', 'Cassius', 'Felix', 'Jesus', 'Aarav', 'Aaron', 'Giovanni',
    'Blaze', 'Korbyn', 'Jonathan', 'Robin', 'Christopher', 'Muhammad', 'Cullen',
]

female_first_names = [
    'Ezra', 'Penny', 'Madison', 'Elaina', 'Lennox', 'Zola', 'Briella', 'Opal',
    'Colette', 'Jaelynn', 'Ivory', 'Gemma', 'Loretta', 'Francesca', 'Sylvia',
    'Madeline', 'Yara', 'Mabel', 'Sloane', 'Vera', 'Dorothy', 'Scarlette',
    'Amira', 'June', 'Raelyn', 'Drew', 'Analia', 'Madelyn', 'Haisley', 'Alaina',
    'Cecilia', 'Megan', 'Veda', 'Kinsley', 'Oakley', 'Cataleya', 'Zaria',
    'Kinley', 'Kailey', 'Maeve', 'Hallie', 'Giana', 'Henley', 'Matilda',
    'Jazmin', 'Rosalyn', 'Ellie', 'Ana', 'Savanna', 'Kimber', 'Reign', 'Flora',
]

last_names = [
    'Stewart', 'Rogers', 'Miller', 'Robinson', 'Martinez', 'Wood', 'Kim',
    'Myers', 'Smith', 'Evans', 'James', 'Campbell', 'Turner', 'Perez',
    'Williams', 'Long', 'Edwards', 'Peterson', 'Alvarez', 'Ortiz', 'Nguyen',
    'Roberts', 'Wilson', 'Lewis', 'Howard', 'Cook', 'Jackson', 'Walker',
    'Clark', 'Martin', 'Brown', 'Johnson', 'Gomez', 'Patel', 'Cruz', 'Reyes',
    'Richardson', 'Thompson', 'King', 'Ramirez', 'Adams', 'White', 'Parker',
    'Sanchez', 'Brooks', 'Scott', 'Sanders', 'Castillo', 'Jones', 'Anderson',
]

Number = Union[int, float]


def clamp(target: Number, low_limit: Number, hi_limit: Number) -> Number:
    """ Clamps input target into the range [low_limit, high_limit]

    @param target: Number
    @param low_limit: Number, must be <= hi_limit
    @param hi_limit: Number, must be >= low_limit
    @return:  Number in range [low_limit, high_limit]

    DocTests
    >>> clamp(10, 1, 100)
    10
    >>> clamp(1, 10, 20)
    10
    >>> clamp(100, 1, 10)
    10
    """
    return min(max(target, low_limit), hi_limit)


def percent_true(percent: int) -> bool:
    return randint(1, 100) <= percent


def random_name(percent_male: int = 50) -> str:
    if percent_true(percent_male):
        first_name = choice(male_first_names)
    else:
        first_name = choice(female_first_names)
    last_name = choice(last_names)
    return f"{first_name} {last_name}"


def random_email(name: str) -> str:
    return f"{name.replace(' ', '.').lower()}@gmail.com"
