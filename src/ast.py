from lexer import Token

from typing import List, Callable

__all__ = [
    'Ast',
    'SpecForm', 'DefineF', 'LambdaF', 'IfF', 'PrognF', 'QuoteF', 'UnquoteF',
    'Sym',
    'Var',
    'Val', 'NumVal', 'IntVal', 'FloatVal', 'StrVal', 'FunVal',
    'Nil',
    'Exp'
]

class Ast(object):
    pass

class Sym(Ast):
    def __init__(self, val: Token):
        self.val = val

    def __str__(self) -> str:
        return str(self.val)

    def __repr__(self) -> str:
        return str(self.val)

    def __eq__(self, other: Ast) -> bool:
        return isinstance(other, Sym) and self.val == other.val

    def __gt__(self, value: Ast) -> bool:
        if type(value) is not Sym:
            raise TypeError("'>' not supported between instances of 'Sym' and '" + str(type(value))[len("<calss '"):-2] + "'")
        return self.val > value.val

    def __hash__(self) -> int:
        return hash(self.val)

class Var(Sym):
    def __init__(self, val: Token):
        super().__init__(val)

class Val(Sym):
    def __init__(self, val: Token):
        super().__init__(val)

class NumVal(Val):
    def __init__(self, val: Token):
        super().__init__(val)

class IntVal(NumVal):
    def __init__(self, val: Token):
        super().__init__(val)

class FloatVal(NumVal):
    def __init__(self, val: Token):
        super().__init__(val)

class StrVal(Val):
    def __init__(self, val: Token):
        super().__init__(val)

class FunVal(Val):
    def __init__(self, fun: Callable[[List[Sym]], Ast]):
        super().__init__(fun)

class Nil(Sym):
    def __init__(self):
        super().__init__('nil')

class Exp(Ast):
    def __init__(self, head: Ast, tail: List[Ast]):
        self.head = head
        self.tail = tail

    def __str__(self) -> str:
        h = str(self.head)
        t = list(map(str, self.tail))
        return "(" + h + " " + " ".join(t) + ")"

class SpecForm(Ast):
    pass

class DefineF(SpecForm):
    def __init__(self, name, val):
        self.name = name
        self.val = val

    def __str__(self):
        return "(define " + str(self.name) + " " + str(self.val) + ")"

class LambdaF(SpecForm):
    def __init__(self, args: List[Sym], body: Ast):
        self.args = args
        self.body = body

    def __str__(self):
        return "(lambda (" + " ".join(list(map(str, self.args))) + ") " + str(self.body) + ")"

class IfF(SpecForm):
    def __init__(self, cond: Ast, true_b: Ast, false_b: Ast):
        self.cond = cond
        self.true_b = true_b
        self.false_b = false_b

    def __str__(self):
        return "(if " + str(self.cond) + " " + str(self.true_b) + " " + str(self.false_b) + ")"

class PrognF(SpecForm):
    def __init__(self, exps: List[Ast]):
        self.exps = exps

    def __str__(self):
        return "(progn " + " ".join(list(map(str, self.exps))) + ")"

class QuoteF(SpecForm):
    def __init__(self, ast: Ast):
        self.ast = ast

    def __str__(self):
        return "(quote " + str(self.ast) + ")"

class UnquoteF(SpecForm):
    def __init__(self, ast: Ast):
        self.ast = ast

    def __str__(self):
        return "(unqoute " + str(self.ast) + ")"
