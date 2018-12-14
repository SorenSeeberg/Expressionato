from typing import List

letters_lower: List[str] = ['a-z']

letters_upper: List[str] = ['A-Z']

integers: List[str] = ['0-9']

alphanum: List[str] = letters_lower + letters_upper + integers

username: List[str] = letters_lower + integers + ['_', '-']

ascii_specials: List[str] = ['_', '#', ';', ':', ',', '<', '>', '(', ')', '[', ']', '{', '}', '%', '&', '$', "'",
                             '`', '"', '~', '.', '@', '=', '+', '-', '*', '\\', '/', '!', '^', '|', ' ']

email_local: List[str] = alphanum + ['!', '#', '$', '%', '&', "'", '*', '+', '-', '/', '=', '?', '^', '_', '`', '{',
                                     '|', '}', '~']

ldh: List[str] = alphanum + ['-']

hexadecimal: List[str] = ['a-f'] + integers
