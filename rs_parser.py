 #!/usr/bin/env python3

import re
from pyparsing import *
import pyparsing as pp

class RobinScriptGrammar():
    ParserElement.setDefaultWhitespaceChars(" \t")

    statement = Forward()
    suite = pp.IndentedBlock(statement)
    all_except_spaces = Word(printables)
    text = Word(printables)
    #literas_spaces = OneOrMore(all_except_spaces | White(' ',max=1))
    #text = pp.Combine(literas_spaces) + ~White()
    #text = alphanums + ".,;!?()\'\" " + ~White()
    
    NL = Suppress(LineEnd())

    input = Word(text)('input')
    output = Word(text)('output')
    in2out = (input + Suppress("=>") + output + NL) ("in2out")
    comment = (Suppress("#") + Word(text) + NL)("comment")

    code = (Optional(NL) + Suppress('{') + Optional(NL) + Word(text) + Optional(NL) + Suppress('}'))('code')
    in2code = (input + Suppress("=>") + code + NL) ("in2code")


    statement << Optional(NL) + Group(in2out | comment | in2code)('statement')
    statement.setResultsName("statement")
    module_body = OneOrMore(statement)

def getRules(pyparserResults):
    rules = []
    for item in pyparserResults:
            if 'in2out' in item:
                input = item['in2out'][0]
                output = item['in2out'][1]
                rules.append({
                    'type': 'answer',
                    'input': input.rstrip(' '),
                    'output': output
                })
            if 'in2code' in item:
                input = item['in2code'][0]
                code = item['in2code'][1]
                rules.append({
                    'type': 'answer',
                    'input': input.rstrip(' '),
                    'code': code
                })
    return rules

        