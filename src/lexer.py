from typing import List, Union, NewType, Any

__all__ = ['Token', 'NestedTokenList', 'tokenize']

Token = NewType('Token', str)
NestedTokenList = Union[Token, List[Any]]

def tokenize(source: str) -> List[Token]:
    tokens = source \
        .replace('(', ' ( ') \
        .replace(')', ' ) ') \
        .replace('\n', '') \
        .replace('\t', '') \
        .split(' ')
    tokens = list(filter(lambda t: t != '', tokens))
    return tokens
