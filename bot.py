 #!/usr/bin/env python3
import ai_engine

state = {}
state['status'] = 'default'
user_message = ""
ai = ai_engine.AI()
ai.isTesting = True
ai.rulesEngine.loadFromFile("script1.rules")

while True:
    answer, state = ai.query(user_message, state)
    if answer != "":
        print(answer)  
    if state['status'] == 'quit':
        break
    user_message = input(">>")
print("Exiting..")

