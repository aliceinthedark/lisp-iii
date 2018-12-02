import built_ins
from ast import *
from environment import Env

from typing import List, Callable

__all__ = ['interpret', 'default_env']

def map_list(f, s):
    return list(map(f, s))

def make_lsp_body(args: List[Sym], body: Ast, e: Env) -> Callable[[List[Sym]], Ast]:
    e = e.extension({})
    def fun(vals: List[Sym]) -> Ast:
        mapped_args = list(zip(args, vals))
        vars_ = {}
        for (k, v) in mapped_args:
            vars_[k] = v
        return interpret(body, e.extension(vars_))
    return FunVal(fun)

def sym_to_bool(sym: Sym) -> bool:
    return sym.val != 'nil' and sym.val != '0'

def handle_spec_form(ast: Ast, e: Env) -> Ast:
    if type(ast) is QuoteF:
        return ast
    elif type(ast) is UnquoteF:
        if type(ast.ast) is not QuoteF:
            raise Exception("Trying to unquote not a quotation.")
        return ast.ast.ast
    elif type(ast) is DefineF:
        e.add_def(interpret(ast.name, e), interpret(ast.val, e))
        return ast.val
    elif type(ast) is LambdaF:
        return make_lsp_body(ast.args, ast.body, e)
    elif type(ast) is IfF:
        if sym_to_bool(interpret(ast.cond, e)):
            return interpret(ast.true_b, e)
        else:
            return interpret(ast.false_b, e)
    elif type(ast) is PrognF:
        for cert_ast in ast.exps[:-1]:
            interpret(cert_ast, e)
        return interpret(ast.exps[-1], e)
    else:
        raise Exception("Unknown form: " + str(ast))
    

def interpret(ast: Ast, e: Env) -> Ast:
    if type(ast) is Exp:
        return e.invoke(interpret(ast.head, e), map_list(lambda a: interpret(a, e), ast.tail))
    elif isinstance(ast, SpecForm):
        return handle_spec_form(ast, e)
    elif type(ast) is Var:
        return e.value(ast)
    elif type(ast) is Sym or isinstance(ast, Val):
        return ast # A symbol evaluates into itself.
    else:
        raise Exception("WHAT THE FUCK HERE!?!?!?: " + str(ast) + " of type " + str(type(ast)))

def default_env():
    return Env({
        Sym('+'): built_ins.sum,
        Sym('-'): built_ins.substraction,
        Sym('*'): built_ins.multiplication,
        Sym('/'): built_ins.division,
        Sym('%'): built_ins.modulo,
        Sym('>'): built_ins.gt,
        Sym('='): built_ins.eq,
    })
