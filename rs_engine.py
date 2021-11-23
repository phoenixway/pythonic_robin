 #!/usr/bin/env python3

from rules import *
from rs_parser import getParser
import rules as rl


class RulesEngine():
    def __init__(self) -> None:
        self.rs_parser = getParser()
        self.rules = []
    
    def get_rules(self, res):
        compound = False
        rules = []
        if ('inner_block' in res) :
            compound = True
            
        for n, item in enumerate(res):
            if compound:
                if n == 0:
                    r = rl.In2Nested_Rule(item[0], item[1])
                    rule = {}
                    rule['type'] = 'compound'
                    rule['first']='In: "{}", out: "{}"'.format(item[0], item[1])
                    rule['inners']=[]
                    r.nested = []
                    continue
                else:
                    r.nested.append(self.get_rules(item))
                    rule['inners'].append(self.get_rules(item))
                    rules = r
                    continue
            elif ('inner_block' in item):
                rules.append(self.get_rules(item))
            else:
                r = rl.In2Out_Rule()
                rule = {}
                rule['type'] = 'solo'
                if isinstance(item, str):
                    r.input = res[0]
                    r.output = res[1]
                    rule['text']= 'In: "{}", out: "{}"'.format(res[0], res[1])
                    rules = r
                    break
                else:
                    r.input = item[0]
                    r.output = item[1]
                    rule['text']= 'In: "{}", out: "{}"'.format(item[0], item[1])
                    rules.append(r)
        return rules

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

