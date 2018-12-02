from ast import *

from typing import List, Dict, Union, NewType, Any, Union, Callable, NoReturn

__all__ = ['Env']

class Env(object):
    def __init__(self, defs: Dict[Sym, Union[Ast, Callable[[Ast, Any], Sym]]]):
        self._defs = defs

    def add_def(self, name: Sym, value: Callable[[Ast], Sym]) -> NoReturn:
        self._defs[name] = value

    def invoke(self, fun: Sym, args: List[Sym]) -> Sym:
        if isinstance(fun, FunVal):
            return fun.val(args)
        if fun not in self._defs:
            raise Exception("Unknown function: " + fun.val)
        if type(self._defs[fun]) is FunVal:
            return self._defs[fun].val(args)
        return self._defs[fun](args, self)

    def value(self, name: Sym) -> Sym:
        if name not in self._defs:
            raise Exception("Undefined variable: " + name.val)
        return self._defs[name]

    def extension(self, defs={}):
        ndefs = dict(self._defs)
        for k in defs:
            ndefs[k] = defs[k]
        return Env(ndefs)
