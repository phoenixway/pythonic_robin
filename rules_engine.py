 #!/usr/bin/env python3

import rs_parser
from pyleri.repeat import Repeat

class RulesEngine():
    def __init__(self) -> None:
        self.grammar = rs_parser.MyGrammar()
        self.rules = []
    
    def loadFromFile(self, name):
        f = open(name, "r")
        script = f.read()
        res = self.grammar.parse(script)
        start = res.tree.children[0] if res.tree.children else res.tree
        if ( type(start.element) is Repeat) and (start.element.name == 'START'):
            for item in start.children:
                rule = rs_parser.get_ast(item)
                if rule != None: self.rules.append(rule)

