 #!/usr/bin/env python3
from string import whitespace
from pyparsing import *
import pyparsing as pp

def getParser():
    ParserElement.setDefaultWhitespaceChars(" \t")
    statement = Forward()
    suite = pp.IndentedBlock(statement)
    NL = Suppress(LineEnd())
    nonspaces=alphanums + "._,:=;%!?#+-()\'\"/"
    nonspacesjs=alphanums + "._,:#=*{}[]!;%!?+-()\'\"/"
    text = Combine(delimitedList(Word(nonspaces), delim=r' '), joinString=' ')
    input = text('input')
    output = text('output')
    in2out = (input + Suppress(Optional(Word(" "))) + Suppress(">>>") + ~FollowedBy("jscode") + output + NL) ("in2out")
    comment = (Suppress("#") + Word(nonspaces + " ") + NL)("comment")

    code = OneOrMore(Optional(NL) + Word(nonspaces + " ") + Optional(NL))('code')

    in2code = (input + Suppress(">>>") + Optional(NL) + Suppress('{') + code + Optional(NL) + Suppress('}') + NL) ("in2code")
    
    
    txt = OneOrMore(Word(nonspacesjs), stop_on="end_jscode")
    jscode = (Optional(NL) + txt + Optional(OneOrMore(NL + txt, stop_on="end_jscode")) + Optional(NL))('jscode')

    in2jscode = (input + Suppress(">>> jscode") + jscode + Suppress(Keyword("end_jscode")))("in2jscode")


    statement << Optional(NL) + Group(in2out | comment | in2code | in2jscode | NL)('statement')
    statement.setResultsName("statement")
    return OneOrMore(statement)