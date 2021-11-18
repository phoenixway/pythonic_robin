 #!/usr/bin/env python3

from string import whitespace
from pyparsing import *
import pyparsing as pp

class RobinScriptParser():
    ParserElement.setDefaultWhitespaceChars(" \t")

    statement = Forward()
    suite = pp.IndentedBlock(statement)
    NL = Suppress(LineEnd())
    nonspaces=alphanums + ".,;!?()\'\""
    text = Combine(delimitedList(Word(nonspaces), delim=r' '), joinString=' ')
    input = text('input')
    output = text('output')
    in2out = (input + Suppress(Optional(Word(" "))) + Suppress("=>") + output + NL) ("in2out")
    comment = (Suppress("#") + Word(nonspaces + " ") + NL)("comment")

    code = (Optional(NL) + Suppress('{') + Optional(NL) + Word(nonspaces + " ") + Optional(NL) + Suppress('}'))('code')
    in2code = (input + Suppress("=>") + code + NL) ("in2code")


    statement << Optional(NL) + Group(in2out | comment | in2code)('statement')
    statement.setResultsName("statement")
    body = OneOrMore(statement)

    def getRules(self, pyparserResults):
        rules = []
        for item in pyparserResults:
                if 'in2out' in item:
                    input = item['in2out'][0]
                    output = item['in2out'][1]
                    rules.append({
                        'type': 'answer',
                        'input': input,
                        'output': output
                    })
                if 'in2code' in item:
                    input = item['in2code'][0]
                    code = item['in2code'][1]
                    rules.append({
                        'type': 'answer',
                        'input': input,
                        'code': code
                    })
        return rules

class RulesEngine():
    def __init__(self) -> None:
        self.parser = RobinScriptParser()
        self.rules = []
    
    def loadFromFile(self, name):
        f = open(name, "r")
        script = f.read()
        self.rules.extend(self.parser.getRules(self.parser.body.parseString(script)))

