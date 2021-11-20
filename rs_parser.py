 #!/usr/bin/env python3
from string import whitespace
from pyparsing import *
import pyparsing as pp

def getParser():
    #ParserElement.setDefaultWhitespaceChars(" \t")
    statement = Forward()
    
    NL = Suppress(LineEnd())
    nonspaces=alphanums + "._,:=;%!?#+-()\'\"/"
    # nonspacesjs=alphanums + "._,:#=*{}[]!;%!?+-()\'\"/"
    text = Word(alphanums + " ")
    input = text('input')
    input.setParseAction(lambda t: t[0].rstrip(' '))
    output = text('output')
    in2out = (input + Suppress(Optional(Word(" "))) + Suppress(">>>") + ~FollowedBy("jscode") + output + NL) ("in2out")
    # text = Combine(delimitedList(Word(nonspaces), delim=r' '), joinString=' ')
    # input = text('input')
    # output = text('output')
    # in2out = (input + Suppress(Optional(Word(" "))) + Suppress(">>>") + ~FollowedBy("jscode") + output + NL) ("in2out")
    # comment = (Suppress("#") + Word(nonspaces + " ") + NL)("comment")

    # code = OneOrMore(Optional(NL) + Word(nonspaces + " ") + Optional(NL))('code')

    # in2code = (input + Suppress(">>>") + Optional(NL) + Suppress('{') + code + Optional(NL) + Suppress('}') + NL) ("in2code")
    
    
    # txt = OneOrMore(Word(nonspacesjs), stop_on="end_jscode")
    # jscode = (Optional(NL) + txt + Optional(OneOrMore(NL + txt, stop_on="end_jscode")) + Optional(NL))('jscode')

    # in2jscode = (input + Suppress(">>> jscode") + jscode + Suppress(Keyword("end_jscode")))("in2jscode")


    # elementBlock = indentedBlock(statement, [1])
    # statement << Optional(NL) + Group(in2out | comment | in2code | in2jscode | NL | elementBlock)('statement')
    # statement.setResultsName("statement")

    
    #elementBlock = Forward()
    # blockContent = statement|elementBlock|comment
    # suite = statement + Optional(indentedBlock(statement, [1]))
           #suite = pp.IndentedBlock(statement)
    #return OneOrMore(statement)

    comment = pythonStyleComment ('comment')
    istack = [1]
#     iblock = (indentedBlock(statement,istack, True))('iblock')
    #iblock = IndentedBlock(statement, recursive=True)('iblock')
    #statement << (Optional(NL) + Group(in2out | comment | iblock ))('statement')
    NESTED_PARENTHESES = nestedExpr('{', '}') ('mark')
    bblock = Suppress(Keyword('{')) + OneOrMore(statement) + Suppress(Keyword('}'))
#     statement << (Group(in2out | comment | bblock ))('statement')
    statement << (Group( text('true text') | NESTED_PARENTHESES ))('statement')


    
    
    return OneOrMore(statement)