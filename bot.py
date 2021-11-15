 #!/usr/bin/env python3
import ai_engine

state = {}
user_message = ""
ai = ai_engine.AI()
ai.isTesting = True
ai.rulesEngine.loadFromFile("script1.rules")

while True:
    status, answer, state = ai.query(user_message, state)
    if answer != "":
        print(answer)  
    if status == 1:
        break
    user_message = input(">>")
print("Exiting..")

