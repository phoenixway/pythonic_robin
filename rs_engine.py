 #!/usr/bin/env python3

from string import whitespace
from pyparsing import *
import pyparsing as pp

from rules import In2Code_Rule, In2Out_Rule  

class RulesEngine():
    def __init__(self) -> None:
        ParserElement.setDefaultWhitespaceChars(" \t")
        statement = Forward()
        suite = pp.IndentedBlock(statement)
        NL = Suppress(LineEnd())
        nonspaces=alphanums + ".,:;%!?+-()\'\""
        text = Combine(delimitedList(Word(nonspaces), delim=r' '), joinString=' ')
        input = text('input')
        output = text('output')
        in2out = (input + Suppress(Optional(Word(" "))) + Suppress("=>") + output + NL) ("in2out")
        comment = (Suppress("#") + Word(nonspaces + " ") + NL)("comment")

        code = OneOrMore(Optional(NL) + Word(nonspaces + " ") + Optional(NL))('code')
        in2code = (input + Suppress("=>") + Optional(NL) + Suppress('{') + code + Optional(NL) + Suppress('}') + NL) ("in2code")

        statement << Optional(NL) + Group(in2out | comment | in2code)('statement')
        statement.setResultsName("statement")
        self.rs_parser = OneOrMore(statement)
        self.rules = []
    
    def getRules(self, pyparserResults):
        rules = []
        for item in pyparserResults:
                if 'in2out' in item:
                    input = item['in2out'][0]
                    output = item['in2out'][1]
                    rules.append(In2Out_Rule(input, output))
                if 'in2code' in item:
                    input = item['in2code'][0]
                    if len(item['in2code']) > 2:
                        i = 1
                        code = []
                        while i < len(item['in2code']):
                            code.append(item['in2code'][i])
                            i=i+1
                    else:
                        code = item['in2code'][1]
                    rules.append(In2Code_Rule(input, code))
        return rules

    def loadFromFile(self, name):
        f = open(name, "r")
        script = f.read()
        self.rules.extend(self.getRules(self.rs_parser.parseString(script)))
