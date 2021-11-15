import grammar_parser
from datetime import datetime
from pyleri.repeat import Repeat

class RulesEngine():
    def __init__(self) -> None:
        script=RulesEngine.loadFromFile("script1.rules")
        my_grammar = grammar_parser.MyGrammar()
        res = my_grammar.parse(script)
        start = res.tree.children[0] if res.tree.children else res.tree
        self.rules = []
        if ( type(start.element) is Repeat) and (start.element.name == 'START'):
            for item in start.children:
                rule = grammar_parser.get_ast(item)
                if rule != None: self.rules.append(rule)
        self.rules.append({
            "type": "answer", 
            "input": "helo", 
            "output": "hey!"
        })
        self.rules.append({"type": "answer", "input": "what?", "output": "dont know"})
        self.rules.append({"type": "func", "input": "time", "func": lambda: datetime.now().strftime("%d/%m/%Y %H:%M:%S")})
        self.rules.append({"type": "answer", "input": "quit", "output": "Have a nice day!"})
        self.rules.append({"type": "answer", "input": "", "output": "Welcome!"})
    
    def loadFromFile(name):
        f = open(name, "r")
        return f.read()
