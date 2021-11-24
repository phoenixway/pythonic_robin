 #!/usr/bin/env python3
from string import whitespace
from pyparsing import *
import pyparsing as pp

def getParser():
    NL=Suppress(LineEnd())
    ONL = Optional(NL)
    LEAD=Suppress(">>>")
    LBRAC, RBRAC = map(Suppress, '{}')
    JSCODE = Suppress(Keyword('jscode'))
    END_JSCODE = Suppress(Keyword('end_jscode'))    
    PYCODE = Suppress(Keyword('pycode'))
    END_PYCODE = Suppress(Keyword('end_pycode'))

    nonspaces=alphanums + "._,:=;%!?#+-()\'\"/"
    text = Word(alphanums + " ")
    input = text('input')
    input.setParseAction(lambda t: t[0].rstrip(' '))
    output = text('output')
    output.setParseAction(lambda t: t[0].rstrip(' '))
  
    in2out = (input + LEAD + ~(JSCODE) + output) ("in2out")

    nonspaces=alphanums + "._,:#=*{}[]!;%!?+-()\'\"/"
    code = ZeroOrMore(Word(nonspaces), stop_on="end_jscode")('jscode')
    code.setParseAction(lambda t: ' '.join(t))

    in2jscode = (input + LEAD + ONL + JSCODE + code + END_JSCODE)("in2jscode")
    
    in2pycode = (input + LEAD + ONL + PYCODE + code + END_PYCODE)("in2pycode")

    nonspacesjs=alphanums + "._,:#=*{}[]!;%!?+-()\'\"/"
    txt = OneOrMore(Word(nonspacesjs), stop_on="end_jscode")
    jscode = (Optional(NL) + txt + Optional(OneOrMore(NL + txt, stop_on="end_jscode")) + Optional(NL))('jscode')
    in2jscode = (input + Suppress(">>> jscode") + jscode + Suppress(Keyword("end_jscode")))("in2jscode")


    comment = pythonStyleComment ('comment')
        
    statement = (Group( comment | in2out | in2jscode | in2pycode ) ).set_results_name('statement', True) 
    
    compound_statement = Forward()('compound_statement')
    inner_block = LBRAC + Optional(NL) + ZeroOrMore(compound_statement | statement) + Optional(NL) + RBRAC
    compound_statement << Group(statement + Optional(NL) + (inner_block('inner_block')))
    compound_statement.set_results_name('compound_statement', True) 
    return OneOrMore(compound_statement | statement)
