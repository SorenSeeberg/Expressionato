from functools import lru_cache
from exp.expressionato import Exp
import exp.character_sequences as cs


@lru_cache(maxsize=2, typed=True)
def simple_email(capped=False) -> Exp:
    """
    Simplistic email expression check. If you need full spec email validation, you must build your own. Building a fully
    compliant email expression is not as easy as one should think.

    https://en.wikipedia.org/wiki/Email_address
    """

    # local: Exp = Exp().negative_look_ahead('^[^.]').sequence(cs.email_local).max(64)
    local: Exp = Exp().sequence(cs.email_local).max(64)
    domain: Exp = Exp().sequence(['.']).sequence(cs.ldh).one_plus()

    exp: Exp = local.string('@').sequence(cs.ldh).one_plus().group(domain).zero_plus()
    exp.config.begin = capped
    exp.config.end = capped

    return exp


@lru_cache(maxsize=2, typed=True)
def username(capped=False, min_length=3, max_length=16) -> Exp:
    """ Alphanum username [A-Za-z0-9] """

    exp: Exp = Exp().sequence(cs.username).between(min_length, max_length)
    exp.config.begin = capped
    exp.config.end = capped

    return exp


@lru_cache(maxsize=2, typed=True)
def password(capped=False, min_length=6, max_length=18) -> Exp:
    """ Alphanum password """

    exp: Exp = Exp().sequence(cs.username).between(min_length, max_length)
    exp.config.begin = capped
    exp.config.end = capped

    return exp


@lru_cache(maxsize=2, typed=True)
def guid(capped=False) -> Exp:
    """ GUID in following format: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx """

    exp: Exp = Exp().sequence(cs.hexadecimal).exactly(8).string('-').sequence(cs.hexadecimal).exactly(4).string(
        '-').sequence(cs.hexadecimal).exactly(4).string('-').sequence(cs.hexadecimal).exactly(4).string(
        '-').sequence(cs.hexadecimal).exactly(12)

    exp.config.begin = capped
    exp.config.end = capped

    return exp


@lru_cache(maxsize=32, typed=True)
def color_hex(capped=False, component_count=6) -> Exp:
    """ Color hex in following format: #xxxxxx """

    exp: Exp = Exp().string('#').sequence(cs.hexadecimal).exactly(component_count)
    exp.config.begin = capped
    exp.config.end = capped

    return exp


@lru_cache(maxsize=1, typed=True)
def byte(capped: bool = False):
    """ Byte 0-255 """
    print("(1?[0-9]{1,2}|2[0-4][0-9]|25[0-5])")

    exp: Exp = Exp().string('1').zero_or_one().sequence(cs.integers).between(1, 2).or_().string('2').sequence(
        '[0-4]').sequence(cs.integers).or_().string('25').sequence('[0-5]')
    exp.config.begin = capped
    exp.config.end = capped

    return exp


def ipv4(capped=False):
    exp: Exp = Exp().group(byte()).string('.').group(byte()).string('.').group(byte()).string('.').group(byte())

    exp.config.begin = capped
    exp.config.end = capped

    return exp



if __name__ == '__main__':
    print(byte())
