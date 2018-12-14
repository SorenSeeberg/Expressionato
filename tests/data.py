from typing import List

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
