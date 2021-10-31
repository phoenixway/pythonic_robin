 #!/usr/bin/env python3
from datetime import date

def get_answer(msg, state):
    status = 0
    answer = "Don't know what to say."
    if msg == "quit":
        status = 1

    rule1 = {"type": "answer", "input": "helo", "output": "hey!"}
    rule2 = {"type": "answer", "input": "what?", "output": "dont know"}
    rule3 = {"type": "func", "input": "time", "func": lambda: (date.today())}
    rule4 = {"type": "answer", "input": "quit", "output": "Have a nice day!"}
    rule5 = {"type": "answer", "input": "", "output": "Welcome!"}

    rules = []
    rules.append(rule1)
    rules.append(rule2)
    rules.append(rule3)
    rules.append(rule4)
    rules.append(rule5)

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

