from lexer import Token, NestedTokenList
from ast import *

from functools import reduce
from typing import List, NoReturn

__all__ = ['parse']

def check_parenthesis(tokens: List[Token]) -> NoReturn:
    open_p = 0
    close_p = 0
    for t in tokens:
        if t == '(':
            open_p += 1
        elif t == ')':
            close_p += 1
    if open_p != close_p:
        raise Exception("Unmatching parenthesis!")

def nest_parenthesis(tokens: List[Token]) -> NestedTokenList:
    check_parenthesis(tokens)
    stack = [[]]
    for t in tokens:
        if t == '(':
            stack.append([])
        elif t == ')':
            t = stack.pop()
            stack[-1].append(t)
        else:
            stack[-1].append(t)
    return stack[0][0]

def map_list(f, l):
    return list(map(f, l))

def astify(l: NestedTokenList) -> Ast:
    if type(l) is list:
        if l == []:
            return Nil()
        elif l[0] == 'quote':
            return QuoteF(astify(l[1]))
        elif l[0] == 'unquote':
            return UnquoteF(astify(l[1]))
        elif l[0] == 'define':
            return DefineF(Sym(l[1]), astify(l[2]))
        elif l[0] == 'lambda':
            if not reduce(lambda a, b: a and isinstance(b, str), l[1], True):
                raise Exception("Lambda arguments should be just symbols, not lists!")
            args = map_list(Sym, l[1])
            return LambdaF(args, astify(l[2]))
        elif l[0] == 'progn':
            return PrognF(map_list(astify, l[1:]))
        elif l[0] == 'if':
            return IfF(astify(l[1]), astify(l[2]), astify(l[3]))
        else:
            head = None
            if type(l[0]) is list:
                head = astify(l[0])
            else:
                head = Sym(l[0])
            return Exp(head, map_list(astify, l[1:]))
    else:
        try:
            return IntVal(str(int(l)))
        except:
            try:
                return FloatVal(str(float(l)))
            except:
                if l.startswith('"') and l.endswith('"'):
                    return StrVal(l[1:-1])
                elif l.startswith("'"):
                    return Sym(l[1:])
                else:
                    return Var(l)

def parse(tokens: List[Token]) -> Ast:
    return astify(nest_parenthesis(tokens))
