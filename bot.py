 #!/usr/bin/env python3
from datetime import datetime

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

