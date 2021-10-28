from typing import List
from .helpers import TOKEN_MAP, Token, TokenType


def what_token(string: str):

    for this_token_name, matcher in TOKEN_MAP.items():
        if match := matcher.match(string):
            return Token(match.group(), this_token_name)

    # if we get to this point,
    # we have some unkown characters
    # just sweep them up until we get to known characters

    for this_token_name, matcher in TOKEN_MAP.items():
        if match := matcher.search(string):
            return Token(string[:match.span()[0]], TokenType.UNKNOWN)

    # if we reach this, it means that the rest of the string contains unknown characters

    return Token(string, TokenType.UNKNOWN)


def lexer(string: str) -> List[Token]:
    string = str(string)

    tokens = []

    while string:
        next_token = what_token(string)
        string = string[len(next_token):]
        tokens.append(next_token)

    return tokens
