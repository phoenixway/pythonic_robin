 #!/usr/bin/env python3
from string import whitespace
from pyparsing import *
import pyparsing as pp

def getParser():
    #ParserElement.setDefaultWhitespaceChars(" \t")
    statement = Forward()
    
    NL = Suppress(LineEnd())
    nonspaces=alphanums + "._,:=;%!?#+-()\'\"/"
    text = Word(alphanums + " ")
    input = text('input')
    input.setParseAction(lambda t: t[0].rstrip(' '))
    output = text('output')
    comment = pythonStyleComment ('comment')
    istack = [1]
    NESTED_PARENTHESES = nestedExpr('{', '}') ('mark')
    statement << (Group( text('true text') | NESTED_PARENTHESES ))('statement')
    return OneOrMore(statement)