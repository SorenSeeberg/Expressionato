from typing import List
from exp.expressionato import Exp
import exp.expressions as expressions
import re


def test_adding_expressions():

    exp_a: Exp = expressions.color_hex(capped=False)
    exp_b: Exp = expressions.guid(capped=False)

    exp_c = exp_a + exp_b
    exp_c.config.begin = True
    exp_c.config.end = True

    assert (str(exp_c) == '\\A#[a-f0-9]{6}[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}\\Z')


def test_negative_look_ahead():
    data = ['Hello World', 'ignoreme', 'Hello Jurassic World', 'ignoreme2']

    exp: Exp = Exp().begin().negative_look_ahead('ignoreme|ignoreme2|ignoremeN').group(
        Exp().sequence(['A-Z', 'a-z', '0-9', ' ']).one_plus()).end()

    found: List[str] = list()

    for item in data:
        result = re.search(str(exp), item)

        if result:
            found.append(result.group())

    assert (len(found) == 2 and found[0] == 'Hello World' and found[1] == 'Hello Jurassic World')

