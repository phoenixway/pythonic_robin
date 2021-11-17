 #!/usr/bin/env python3

import rs_parser

class RulesEngine():
    def __init__(self) -> None:
        self.grammar = rs_parser.RobinScriptGrammar()
        self.rules = []
    
    def loadFromFile(self, name):
        f = open(name, "r")
        script = f.read()
        self.rules.extend(rs_parser.getRules(self.grammar.module_body.parseString(script)))

