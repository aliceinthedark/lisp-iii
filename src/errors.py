from typing import Type, Union
from ast import *

__all__ = ['ArgTypeError']

class ArgTypeError(Exception):
    """
    Example:
    ```
    if not isinstance(a, IntVal):
        raise ArgTypeError(a, type(IntVal))
    ```
    """
    def __init__(self, value: Ast, needed: Type):
        t1 = str(type(value))[len("<class '"):-2]
        t2 = str(needed)[len("<class '"):-2]
        super().__init__("Value of a wrong type " + t1 + ": " + str(value) + ". Should be " + t2)

class FuncArityError(Exception):
    """
    Example:
    ```
    if len(args) < 2:
        raise FuncArityError("sum", ">= 2")
    ```
    """
    def __init__(self, fname: str, arity: Union[int]):
        super().__init__("Function " + fname + " has arity of " + str(arity))
