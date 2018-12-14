from typing import List
import random

"""https://en.wikipedia.org/wiki/Email_address"""
valid_emails: List[str] = [
    'simple@example.com',
    'very.common@example.com',
    'disposable.style.email.with+symbol@example.com',
    'other.email-with-hyphen@example.com',
    'fully-qualified-domain@example.com',
    'user.name+tag+sorting@example.com',
    'x@example.com',
    'example-indeed@strange-example.com',
    'admin@mailserver1',
    'example@s.example',
    '" "@example.org',
    '"john..doe"@example.org'
]

"""https://en.wikipedia.org/wiki/Email_address"""
invalid_emails: List[str] = [
    'Abc.example.com',
    'A@b@c@example.com',
    'a"b(c)d,e:f;g<h>i[j\\k]l@example.com',
    'just"not"right@example.com',
    'this is"not\\allowed@example.com',
    'this\\ still\"not\\allowed@example.com',
    '1234567890123456789012345678901234567890123456789012345678901234+x@example.com',
    'john..doe@example.com',
    'john.doe@example..com',
    '.john.doe@example.com',
    'john.doe.@example.com'
]


def fake_random_guid() -> str:
    def random_digit(length: int) -> str:
        nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']

        return ''.join([random.choice(nums) for x in range(length)])

    return f'{random_digit(8)}-{random_digit(4)}-{random_digit(4)}-{random_digit(4)}-{random_digit(12)}'
