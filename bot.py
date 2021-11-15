 #!/usr/bin/env python3
import ai_engine

state = {}
user_message = ""
while True:
    status, answer, state = ai_engine.get_answer(user_message, state)
    if answer != "":
        print(answer)  
    if status == 1:
        break
    user_message = input(">>")
print("Exiting..")

