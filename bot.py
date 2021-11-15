 #!/usr/bin/env python3
import ai_engine

state = {}
user_message = ""
ai = ai_engine.AI()
while True:
    status, answer, state = ai.get_answer(user_message, state)
    if answer != "":
        print(answer)  
    if status == 1:
        break
    user_message = input(">>")
print("Exiting..")

