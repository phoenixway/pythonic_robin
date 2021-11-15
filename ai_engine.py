 #!/usr/bin/env python3

from rules_engine import RulesEngine
from datetime import datetime

rules_engine = RulesEngine()
rules_engine.loadFromFile("script1.rules")

rules_engine.rules.append({
    "type": "answer", 
    "input": "hello", 
    "output": "hey!"
})
rules_engine.rules.append({
    "type": "func", 
    "input": "time", 
    "func": lambda: datetime.now().strftime("%d/%m/%Y %H:%M:%S")
})
rules_engine.rules.append({"type": "answer", "input": "quit", "output": "Have a nice day!"})
rules_engine.rules.append({"type": "answer", "input": "", "output": "Welcome!"})
rules_engine.rules.append({"type": "answer", "input": "what?", "output": "dont know"})


def get_answer(msg, state):
    answer = "Don't know what to say."
    status = 1 if msg == "quit" else 0 

    for rule in rules_engine.rules:
        if rule["type"] == "answer" and rule["input"] == msg:
            answer = rule["output"]
            break
        elif rule["type"] == "func" and rule["input"] == msg:
            answer = rule["func"]()
            break

    return status, answer, state