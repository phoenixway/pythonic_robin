 #!/usr/bin/env python3

from rules import *
from rs_parser import getParser

class RulesEngine():
    def __init__(self) -> None:
        self.rs_parser = getParser()
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
                if 'in2jscode' in item:
                    input = item['in2jscode'][0]
                    s = ""
                    for i in item['jscode']:
                        s = s + i + " "
                    code = s
                    rules.append(In2JSCode_Rule(input, code))
        return rules

    def loadFromFile(self, name):
        try:
            with open(name, "r") as f:
                script = f.read()
        except Exception:
            print("Error script reading.")
        else:
            self.rules.extend(self.getRules(self.rs_parser.parseString(script)))

