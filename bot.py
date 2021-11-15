 #!/usr/bin/env python3
from rules_engine import RulesEngine

rules = RulesEngine().rules

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

