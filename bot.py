 #!/usr/bin/env python3

import re

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

class MyGrammar(Grammar):
    #RE_KEYWORDS = re.compile(r'\S+')
    RE_KEYWORDS = re.compile('^[A-Za-z-=>]+')
    r_output = Regex('[a-zA-Z 0-9\']+')
    r_input = Regex('[a-zA-Z 0-9\']+')

    # r_output = Regex('(?:"(?:[^"]*)")+')
    # r_input = Regex('(?:"(?:[^"]*)")+')
    k_lead2 = Token('=>')
    START = Repeat(Sequence(r_input, k_lead2, r_output))

# Compile your grammar by creating an instance of the Grammar Class.
my_grammar = MyGrammar()

# Use the compiled grammar to parse 'strings'
print(my_grammar.parse('text => Iris').is_valid) # => True
print(my_grammar.parse('bye "Iris"').is_valid) # => False
print(my_grammar.parse('text => Iris').as_str()) # => True
print(my_grammar.parse('text => Iris')) # => True
res = my_grammar.parse('text => Iris\ntext2 => TT2')
start = res.tree
#res.tree.children[0].element.name
#res.tree.element.name
#res.tree.element Repeat
#res.tree.children[0].element Repeat
#res.tree.children[0].children[0].element #Sequence
#далі вже є ім'я і тип відповідає складовим statement`a
print(grammar_parser.node_props(start, start.children))

#print(my_grammar.parse('bye "Iris"').as_str()) # => error at position 0, expecting: hi

def get_answer(msg, state):
    answer = "Don't know what to say."
    status = 1 if msg == "quit" else 0 

    rules = []
    rules.append({
        "type": "answer", 
        "input": "helo", 
        "output": "hey!"
    })
    rules.append({"type": "answer", "input": "what?", "output": "dont know"})
    rules.append({"type": "func", "input": "time", "func": lambda: datetime.now().strftime("%d/%m/%Y %H:%M:%S")})
    rules.append({"type": "answer", "input": "quit", "output": "Have a nice day!"})
    rules.append({"type": "answer", "input": "", "output": "Welcome!"})

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

