 #!/usr/bin/env python3

def get_answer(msg, state):
    status = 0
    answer = ""
    if msg == "quit":
        status = 1
    script = {}
    script[""] = "Welcome!"
    script["quit"] = "Have a nice day!"
    answer = script[msg] if msg in script else "Don't know what to say."
    print(answer)
    return status, answer, state

state = {}
m = ""
while True:
    s, _, state = get_answer(m, state)
    if s == 1:
        break
    m = input(">>")
print("Exiting..")

