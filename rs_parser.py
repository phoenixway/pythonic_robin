 #!/usr/bin/env python3
from string import whitespace
from pyparsing import *
import pyparsing as pp

def getParser():
    #ParserElement.setDefaultWhitespaceChars(" \t")
    statement = Forward()
    NL=Suppress(LineEnd())
    LEAD=Suppress(">>>")
    nonspaces=alphanums + "._,:=;%!?#+-()\'\"/"
    text = Word(alphanums + " ")
    just_text = text('just_text')  + ~FollowedBy(LEAD)
    input = text('input')
    input.setParseAction(lambda t: t[0].rstrip(' '))
    output = text('output')
    in2out = (input + Suppress(Optional(Word(" "))) + LEAD + output + NL) ("in2out")
    comment = pythonStyleComment ('comment')
    NESTED_PARENTHESES = nestedExpr('{', '}').set_results_name('nested', True)
    statement << (Group( comment | just_text | in2out)).set_results_name('statement', True)
    s = (statement + Optional(NESTED_PARENTHESES))
    #statement()
    return OneOrMore(s)