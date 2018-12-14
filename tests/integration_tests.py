from tests.data import valid_emails, invalid_emails
from typing import List
from exp.expressionato import Exp
import exp.expressions as expressions
import re


def test_valid_emails():
    success: int = 0
    failure: int = 0

    for email_string in valid_emails:
        result = re.search(str(expressions.simple_email(capped=True)), email_string)
        if result:
            success += 1
        else:
            failure += 1
            print('FAIL: ', email_string)

    if failure > 0:
        print(success, failure)

    assert (success == 12 and failure == 0)


def test_invalid_emails():
    success: int = 0
    failure: int = 0

    for email_string in invalid_emails:
        result = re.search(str(expressions.simple_email(capped=True)), email_string)
        if result:
            success += 1
        else:
            failure += 1

    assert (success == 10 and failure == 1)

