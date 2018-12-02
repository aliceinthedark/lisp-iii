#!/usr/bin/env python

from lexer import *
from lsp_parser import *
from interpreter import *

import sys
import traceback

def run(source):
    env = default_env()
    return interpret(parse(tokenize(source)), env)

def are_parenthesis_not_closed(src):
    o = 0
    c = 0
    for t in tokenize(src):
        if t == '(': o += 1
        elif t == ')': c += 1
    return o > c

def run_repl():
    inp = input("% ")
    while inp != '(exit)':
        try:
            if are_parenthesis_not_closed(inp):
                inp += " " + input("> ")
            else:
                print(run(inp))
                inp = input("% ")
        except Exception as e:
            traceback.print_tb(e.__traceback__)
            print(str(sys.exc_info()[0])[len("<class '"):-2] + ": " + str(e))
            inp = input("% ")

def run_file():
    with open(sys.argv[1]) as f:
        print(run(f.read()))

def main():
    if len(sys.argv) == 2:
        run_file()
    else:
        run_repl()

if __name__ == '__main__':
    main()
