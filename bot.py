 #!/usr/bin/env python3

def get_answer(msg, state):
    status = 0
    answer = ""
    if msg == "quit":
        status = 1
    script = {}
    script[""] = "Welcome!"
    script["hey"] = "hello"
    answer = script[msg] if msg in script else "Don't know what to say."
    print(answer)
    return status, answer

state = {}
m = ""
while True:
    s, a = get_answer(m, state)
    if s == 1:
        break
    m = input(">>")
print("Bye")

