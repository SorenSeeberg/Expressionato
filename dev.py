import re
import exp.expressions as expressions


def validate_emails(emails) -> None:
    for email_string in emails:
        result = re.search(str(expressions.simple_email(capped=True)), email_string)
        if result:
            print(result.group())
        else:
            print(f'FAIL : {email_string}')


if __name__ == '__main__':
    # name = Expressionato().sequence('A-Za-z').one_plus()
    # age = Expressionato().sequence('0-9').between(1, 3)
    # name_and_age = Expressionato().begin().string('name:').group(name).string('age:').group(age).end()
    # print(name_and_age)
    #
    # expression = Expressionato().begin().sequence('A-Za-z0-9_%/').one_plus().end()
    # print(re.compile(str(expression)))
    # print(re.compile('\\A[A-Za-z0-9_%/]+\\Z'))

    email = re.compile(str(expressions.simple_email))
    emails_valid = ["soren.seeberg77@gmail.com",
                    "soren.seeberg.77@gmail.com",
                    "soren.[seeberg]@mail.co.uk",
                    "email@example.com",
                    "firstname.lastname@example.com",
                    "email@subdomain.example.com",
                    "firstname+lastname@example.com",
                    "email@123.123.123.123",
                    "email@[123.123.123.123]",
                    '"email"@example.com',
                    "1234567890@example.com",
                    "email@example-one.com",
                    "_______@example.com",
                    "email@example.name",
                    "email@example.museum",
                    "email@example.co.jp",
                    "firstname-lastname@example.com"]

    emails_valid_strange = ['much."more\ unusual"@example.com',
                            'very.unusual."@".unusual.com @ example.com',
                            r'very."(),:; <> []".VERY."very @\\ "very".unusual@strange.example.com']

    emails_invalid = [".soren.seeberg@gmail.com",
                      "soren.seeberg.@gmail.com",
                      'plainaddress',
                      '#@%^%#$@#$@#.com',
                      '@example.com',
                      "Joe Smith <email@example.com>",
                      "email.example.com",
                      "email@example@example.com",
                      ".email@example.com",
                      "email.@example.com",
                      "email..email@example.com",
                      "あいうえお@example.com",
                      "email@example.com (Joe Smith)",
                      "email@example",
                      "email@-example.com",
                      "email@example.web",
                      "email@111.222.333.44444",
                      "email@example..com",
                      "Abc..123@example.com"
                      ]

    emails_invalid_strange = ['"(),:;<>[\]@example.com',
                              'just"not"right@example.com',
                              r'this\ is"really"not\allowed@example.com']

    guid = '123e4567-e89b-12d3-a456-426655440000'

    result = re.search(str(expressions.guid), guid)
    if result:
        print(result.group())
    else:
        print(f'FAIL: {guid}')

    print()
    print(expressions.simple_email())
    print(expressions.color_hex())
    print(expressions.simple_email())
    print(expressions.guid())

    print('\nvalid\n')
    validate_emails(emails_valid)
    print('\nvalid - strange\n')
    validate_emails(emails_valid_strange)
    # print('\ninvalid\n')
    # validate_emails(emails_invalid)
    # print('\ninvalid - strange\n')
    # validate_emails(emails_invalid_strange)