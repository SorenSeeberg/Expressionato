from functools import lru_cache
from exp.expressionato import Exp
import exp.character_sequences as cs


@lru_cache(maxsize=128, typed=True)
def simple_email(capped=False) -> Exp:
    """
    Simplistic email expression check. If you need full spec email validation, you must build your own. Building a fully
    compliant email expression is not as easy as one should think.

    https://en.wikipedia.org/wiki/Email_address
    """

    local: Exp = Exp().negative_look_ahead('^[^.]').sequence(cs.email_local).max(64)
    domain: Exp = Exp().sequence(['.']).sequence(cs.ldh).one_plus()

    if capped:
        Exp().begin().insert(local).string('@').sequence(cs.ldh).one_plus().group(domain).zero_plus().end()

    return local.string('@').sequence(cs.ldh).one_plus().group(domain).zero_plus()


@lru_cache(maxsize=128, typed=True)
def username(capped=False, min_length=3, max_length=16) -> Exp:
    """ Alphanum username [A-Za-z0-9] """
    if capped:
        return Exp().begin().sequence(cs.username).between(min_length, max_length).end()
    else:
        return Exp().sequence(cs.username).between(min_length, max_length)


@lru_cache(maxsize=128, typed=True)
def password(capped=False, min_length=6, max_length=18) -> Exp:
    """ Alphanum password """
    if capped:
        return Exp().begin().sequence(cs.username).between(min_length, max_length).end()
    else:
        return Exp().sequence(cs.username).between(min_length, max_length)


@lru_cache(maxsize=128, typed=True)
def guid(capped=False) -> Exp:
    """ GUID in following format: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx """

    if capped:
        return Exp().begin().sequence(cs.hexadecimal).exactly(8).string('-').sequence(cs.hexadecimal).exactly(4).string(
            '-').sequence(cs.hexadecimal).exactly(4).string('-').sequence(cs.hexadecimal).exactly(4).string(
            '-').sequence(
            cs.hexadecimal).exactly(12).end()
    else:
        return Exp().sequence(cs.hexadecimal).exactly(8).string('-').sequence(cs.hexadecimal).exactly(4).string(
            '-').sequence(cs.hexadecimal).exactly(4).string('-').sequence(cs.hexadecimal).exactly(4).string(
            '-').sequence(
            cs.hexadecimal).exactly(12)


@lru_cache(maxsize=128, typed=True)
def color_hex(capped=False, component_count=6) -> Exp:
    """ Color hex in following format: #xxxxxx """
    if capped:
        return Exp().begin().string('#').sequence(cs.hexadecimal).exactly(component_count).end()
    else:
        return Exp().string('#').sequence(cs.hexadecimal).exactly(component_count)
