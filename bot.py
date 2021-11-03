 #!/usr/bin/env python3

from pyleri.repeat import Repeat
import grammar_parser
from datetime import datetime
from pyleri import (
    Grammar,
    Keyword,
    Token,
    Regex,
    List, 
    Sequence)

f = open("script1.rules", "r")
script = f.read()

my_grammar = grammar_parser.MyGrammar()
res = my_grammar.parse(script)
start = res.tree.children[0] if res.tree.children else res.tree
rules = []
if ( type(start.element) is Repeat) and (start.element.name == 'START'):
    for item in start.children:
        rule = grammar_parser.get_ast(item)
        if rule != None: rules.append(rule)

rules.append({
    "type": "answer", 
    "input": "helo", 
    "output": "hey!"
})
rules.append({"type": "answer", "input": "what?", "output": "dont know"})
rules.append({"type": "func", "input": "time", "func": lambda: datetime.now().strftime("%d/%m/%Y %H:%M:%S")})
rules.append({"type": "answer", "input": "quit", "output": "Have a nice day!"})
rules.append({"type": "answer", "input": "", "output": "Welcome!"})

def get_answer(msg, state):
    answer = "Don't know what to say."
    status = 1 if msg == "quit" else 0 

    for rule in rules:
        if rule["type"] == "answer" and rule["input"] == msg:
            answer = rule["output"]
            break
        elif rule["type"] == "func" and rule["input"] == msg:
            answer = rule["func"]()
            break

    return status, answer, state

state = {}
m = ""
while True:
    s, a, state = get_answer(m, state)
    if a != "":
        print(a)  
    if s == 1:
        break
    m = input(">>")
print("Exiting..")

