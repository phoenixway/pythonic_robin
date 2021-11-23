 #!/usr/bin/env python3
from string import whitespace
from pyparsing import *
import pyparsing as pp

def getParser():
    #ParserElement.setDefaultWhitespaceChars(" \t")
    #statement = Forward()

    NL=Suppress(LineEnd())
    LEAD=Suppress(">>>")
    LBRAC, RBRAC = map(Suppress, '{}')
    
    text = Word(alphanums + " ")

    just_text = text('just_text')  + ~FollowedBy(LEAD)
    
    input = text('input')
    input.setParseAction(lambda t: t[0].rstrip(' '))
    output = text('output')
    in2out = (input + LEAD + output) ("in2out")

    comment = pythonStyleComment ('comment')
        
    statement = (Group( comment | just_text | in2out) ).set_results_name('statement', True) 
    
    compound_statement = Forward()('compound_statement')
    inner_block = LBRAC + Optional(NL) + ZeroOrMore(compound_statement | statement) + Optional(NL) + RBRAC
    compound_statement << Group(statement + Optional(NL) + (inner_block('inner_block')))
    compound_statement.set_results_name('compound_statement', True) 
#     compound_statement = Forward()
#     compound_statement = statement('outer_statement') + Optional(NL) + LBRAC + Optional(OneOrMore(compound_statement | (statement  + ~FollowedBy(LBRAC))))('inner_block') + Optional(NL) + RBRAC
#     compound_statement.set_debug()

    return OneOrMore(compound_statement | statement)