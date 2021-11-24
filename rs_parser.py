 #!/usr/bin/env python3
from string import whitespace
from pyparsing import *
import pyparsing as pp

def getParser():
    NL=Suppress(LineEnd())
    LEAD=Suppress(">>>")
    LBRAC, RBRAC = map(Suppress, '{}')
    
    text = Word(alphanums + " ")

    #just_text = text('just_text')  + ~FollowedBy(LEAD)
    
    input = text('input')
    input.setParseAction(lambda t: t[0].rstrip(' '))
    output = text('output')
    output.setParseAction(lambda t: t[0].rstrip(' '))
    in2out = (input + LEAD + output) ("in2out")

    nonspacesjs=alphanums + "._,:#=*{}[]!;%!?+-()\'\"/"
    txt = OneOrMore(Word(nonspacesjs), stop_on="end_jscode")
    jscode = (Optional(NL) + txt + Optional(OneOrMore(NL + txt, stop_on="end_jscode")) + Optional(NL))('jscode')
    in2jscode = (input + Suppress(">>> jscode") + jscode + Suppress(Keyword("end_jscode")))("in2jscode")


    comment = pythonStyleComment ('comment')
        
    statement = (Group( comment | in2out | in2jscode ) ).set_results_name('statement', True) 
    
    compound_statement = Forward()('compound_statement')
    inner_block = LBRAC + Optional(NL) + ZeroOrMore(compound_statement | statement) + Optional(NL) + RBRAC
    compound_statement << Group(statement + Optional(NL) + (inner_block('inner_block')))
    compound_statement.set_results_name('compound_statement', True) 
    return OneOrMore(compound_statement | statement)