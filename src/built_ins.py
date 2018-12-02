from ast import *
from errors import *

from functools import reduce

def sum(args, e):
    if len(args) < 1:
        raise FuncArityError("+", ">= 1")
    def summer(a, b):
        if not isinstance(b, IntVal):
            raise ArgTypeError(b, IntVal)
        return a + int(b.val)
    return Val(str(reduce(summer, args, 0)))

def substraction(args, e):
    if len(args) < 1:
        raise FuncArityError("-", ">= 1")
    if isinstance(args[0], IntVal):
        raise ArgTypeError(args[0], IntVal)
    def substractor(a, b):
        if not isinstance(b, IntVal):
            raise ArgTypeError(b, IntVal)
        return a - int(b.val)
    return Val(str(reduce(substractor, args[1:], int(args[0].val))))

def multiplication(args, e):
    if len(args) < 2:
        raise FuncArityError("*", ">= 2")
    def multiplicator(a, b):
        if not isinstance(b, IntVal):
            raise ArgTypeError(b, IntVal)
        return a * int(b.val)
    return Val(str(reduce(multiplicator, args, 1)))

def division(args, e):
    if len(args) < 2:
        raise FuncArityError("/", ">= 2")
    if isinstance(args[0], IntVal):
        raise ArgTypeError(args[0], IntVal)
    def divider(a, b):
        if not isinstance(b, IntVal):
            raise ArgTypeError(b, IntVal)
        return a / int(b.val)
    return Val(str(reduce(divider , args[1:], int(args[0].val))))

def modulo(args, e):
    if len(args) < 2:
        raise FuncArityError("%", ">= 2")
    if isinstance(args[0], IntVal):
        raise ArgTypeError(args[0], IntVal)
    def modulator(a, b):
        if not isinstance(b, IntVal):
            raise ArgTypeError(b, IntVal)
        return a % int(b)
    return IntVal(str(reduce(modulator, args[1:], int(args[0].val))))

def gt(args, e):
    return Val(str(int(args[0].val) > int(args[1].val)))

def eq(args, e):
    return Sym('t') if args[0] == args[1] else Nil()
