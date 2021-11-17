 #!/usr/bin/env python3

import re
from pyparsing import *
import pyparsing as pp

class RobinScriptGrammar():
    statement = Forward()
    #suite = indentedBlock(statement)
    text = alphanums + ".,!? "
    input = Word(text)('input')
    output = Word(text)('output')
    input2output = (input + Suppress("=>") + output) ("in2out")
    comment = ("#" + Word(text))("comment")
    statement << Group(input2output | comment)('statement')
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
    return rules

        