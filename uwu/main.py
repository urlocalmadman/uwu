from typing import List
from .helpers import REPLACE_WORDS_MAP, RANDOM_INSERTS, Token, TokenType
from .lexer import lexer
from random import random, choice


def replace_word(token: Token):
    if token.token_type == TokenType.LETTERS and token.val in REPLACE_WORDS_MAP:
        return Token(REPLACE_WORDS_MAP[token.val], token.token_type)

    return token


def replace_chars(token: Token) -> Token:
    return Token(
        ''.join(
            char.replace('l', 'w').replace('r', 'w').replace('L', 'W').replace('R', 'W')
            if (random() < 0.75) and ('lol' not in token.val)
            else char
            for char
            in token.val
        ),
        token.token_type
    )


def uwuify(string: str) -> str:
    tokens = lexer(str(string))

    # process individual tokens with functions that don't depend on adjacent tokens
    partially_processed_tokens = [
        replace_chars(replace_word(token))
        for token
        in tokens
    ]

    processed_tokens: List[Token] = []

    for index, token in enumerate(partially_processed_tokens):
        is_last = index == len(partially_processed_tokens) - 1
        is_space = token.token_type == TokenType.SPACE
        is_letter = token.token_type == TokenType.LETTERS

        next_token = (partially_processed_tokens[index + 1]
                      if index < len(partially_processed_tokens) - 1
                      else None)

        prev_token = (partially_processed_tokens[index - 1]
                      if index > 0
                      else None)

        # stutters

        if (not is_last) and random() < 0.05 and is_space and next_token \
                and next_token.token_type == TokenType.LETTERS and len(next_token.val) > 1:
            token = Token(
                token.val + next_token.val[:1] + '-',
                TokenType.LETTERS
            )

        # nyaaa

        if prev_token and prev_token.token_type == TokenType.SPACE \
                and is_letter and token.val.startswith('n'):
            token = Token(
                token.val[0] + 'y' + token.val[1:], token_type=TokenType.LETTERS
            )

        if prev_token and prev_token.token_type == TokenType.SPACE \
                and is_letter and token.val.startswith('N'):
            token = Token(
                token.val[0] + 'Y' + token.val[1:], token_type=TokenType.LETTERS
            )

        # kaomoji

        if random() < 0.3:
            if next_token and prev_token:
                # after punctuation
                if prev_token.token_type == TokenType.PUNCTUATION and len(prev_token.val) < 4:
                    token = Token(choice(RANDOM_INSERTS) + token.val,
                                  token_type=TokenType.LETTERS)

                elif (
                        prev_token.token_type == TokenType.SPACE and prev_token.val[-1:] == '\n'
                ):
                    # after newlines
                    try:
                        curr_last_token = processed_tokens[-1]
                        processed_tokens[-1] = Token(
                            curr_last_token.val.rstrip(),
                            token_type=curr_last_token.token_type
                        )
                        token = Token(
                            choice(RANDOM_INSERTS) + '\n' + token.val,
                            token_type=TokenType.LETTERS
                        )
                    except IndexError:
                        pass
            else:
                # we're on the last token
                if token.token_type != TokenType.PUNCTUATION:
                    token = Token(
                        token.val.rstrip()+' '+choice(RANDOM_INSERTS),
                        token_type=TokenType.LETTERS
                    )
        processed_tokens.append(token)

    return ''.join(token.val for token in processed_tokens)
