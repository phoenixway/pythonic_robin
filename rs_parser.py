 #!/usr/bin/env python3

import re
from pyparsing import *
import pyparsing as pp

class RobinScriptGrammar():
    statement = Forward()
    suite = pp.IndentedBlock(statement)
    text = alphanums + ".,!?()\'\" "
    input = Word(text)('input')
    output = Word(text)('output')
    code = (Suppress('{') + Word(text) + Suppress('}'))('code')
    input2output = (input + Suppress("=>") + output) ("in2out")
    input2code = (input + Suppress("=>") + code ) ("in2code")
    comment = ("#" + Word(text))("comment")
    statement << Group(input2output | comment | input2code)('statement')
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

        