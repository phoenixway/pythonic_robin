 #!/usr/bin/env python3
import ai_engine

state = {}
m = ""
while True:
    s, a, state = ai_engine.get_answer(m, state)
    if a != "":
        print(a)  
    if s == 1:
        break
    m = input(">>")
print("Exiting..")

