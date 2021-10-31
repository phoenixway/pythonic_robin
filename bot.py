 #!/usr/bin/env python3

def get_answer(msg, state):
    status = 0
    answer = ""
    if msg == "quit":
        status = 1
    script = {}
    script[""] = lambda: print("Welcome, sir!")
    script["hey"] = lambda: print("hello")
    script["quit"] = lambda: print("Have a nice day!")
    if msg in script:
        script[msg]()
    else:
        print("Don't know what to say.")
    return status, answer

state = {}
m = ""
while True:
    s, a = get_answer(m, state)
    if s == 1:
        break
    m = input(">>")
print("Bye")

