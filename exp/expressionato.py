from dataclasses import dataclass
from typing import List
import exp.character_sequences as cs


# https://www.debuggex.com/cheatsheet/regex/python

@dataclass
class ExpConfig:

    begin: bool = False
    end: bool = False


class Exp:
    """ Expressionato """

    def __init__(self, config: ExpConfig = ExpConfig()):
        self.config: ExpConfig = config
        self.__re_fragments: List[str] = list()

    @staticmethod
    def __resolve_input(value) -> str:
        if not isinstance(value, str):
            return value.get_table_name()

        return value

    def __repr__(self) -> str:
        begin = ['\\A'] if self.config.begin else ['']
        end = ['\\Z'] if self.config.begin else ['']

        return r''.join(begin + self.__re_fragments + end)

    def __str__(self) -> str:

        return self.__repr__()

    def __add__(self, other: 'Exp') -> 'Exp':
        new_expressions = Exp()
        new_expressions.__re_fragments = self.__re_fragments + other.__re_fragments
        return new_expressions

    def group(self, expression: 'exp', capture: bool = True, name: str = None):
        """ Groups """

        if name:
            pre = f'?P<{name}>'
        elif capture:
            pre = ''
        else:
            pre = '?:'

        self.__re_fragments.append(f'({pre}{str(expression)})')

        return self

    def insert(self, expression: 'exp'):
        """ Weld in other expression """

        self.__re_fragments.append(str(expression))

        return self

    def begin(self, ignore_flags: bool = False):
        """ Assertion: Beginning of line '\\A' or '^' """
        if ignore_flags:
            self.__re_fragments.append('\\A')
        else:
            self.__re_fragments.append('^')
        return self

    def end(self, ignore_flags: bool = False):
        """ Assertion: End of line '\\Z' or '$' """
        if ignore_flags:
            self.__re_fragments.append('\\Z')
        else:
            self.__re_fragments.append('$')
        return self

    def digit(self):
        """ Digit character '\\d' """
        self.__re_fragments.append('\\d')
        return self

    def non_digit(self):
        """ Character Class: Non digit character '\\D' """
        self.__re_fragments.append('\\D')
        return self

    def white_space(self):
        """ Character Class: White space character '\\s' """
        self.__re_fragments.append('\\s')
        return self

    def non_white_space(self):
        """ Character Class: Non white space character '\\S' """
        self.__re_fragments.append('\\S')
        return self

    def word_char(self):
        """ Character Class: Word character '\\w' """
        self.__re_fragments.append('\\w')
        return self

    def non_word_char(self):
        """ Character Class: Non word character '\\W' """
        self.__re_fragments.append('\\W')
        return self

    def string(self, string: str):
        """ Basics: fixed string of characters """
        self.__re_fragments.append(string)
        return self

    def or_(self):
        self.__re_fragments.append('|')
        return self

    def sequence(self, sequence: List[str]):
        sequence_string: str = "".join(f'\\{hex(ord(char))[1:]}' if len(char) == 1 else char for char in sequence)
        self.__re_fragments.append(f'[{sequence_string}]')
        return self

    def any_char(self):
        """ Basics: Any char except newline '.' """
        self.__re_fragments.append('.')

    def alphanum(self):
        """ Helper: sequence string 'A-Za-z0-9' """
        self.sequence(cs.alphanum)
        return self

    def seq_ascii(self):
        """ Helper: sequence string 'A-Za-z0-9' """
        self.sequence(cs.alphanum + cs.ascii_specials)
        return self

    def zero_plus(self):
        """ Quantifier: 0 or more '*' """
        self.__re_fragments.append('*')
        return self

    def one_plus(self):
        """ Quantifier: 1 or more '+' """
        self.__re_fragments.append('+')
        return self

    def zero_or_one(self):
        """ Quantifier: 0 or 1 '?' """
        self.__re_fragments.append('?')
        return self

    def max(self, count: int):
        """ Quantifier: up to x '{,x}' """
        self.__re_fragments.append(f'{{,{count}}}')
        return self

    def min(self, count: int):
        """ Quantifier: x or more '{x,}' """
        self.__re_fragments.append(f'{{{count},}}')
        return self

    def exactly(self, count: int):
        """ Quantifier: exactly x '{x}'"""
        self.__re_fragments.append(f'{{{count}}}')
        return self

    def between(self, count_min: int, count_max: int):
        """ Quantifier: x to y '{x, y}' """
        self.__re_fragments.append(f'{{{count_min},{count_max}}}')
        return self

    def look_ahead(self, string):
        """ Assertion: """
        self.__re_fragments.append(f'(?={string})')
        return self

    def look_behind(self, string: str):
        """ Assertion: """
        self.__re_fragments.append(f'(?<={string})')
        return self

    def negative_look_ahead(self, string: str):
        """ Assertion: """
        self.__re_fragments.append(f'(?!{string})')
        return self

    def negative_look_behind(self, string: str):
        """ Assertion: """
        self.__re_fragments.append(f'(?<!{string})')
        return self
