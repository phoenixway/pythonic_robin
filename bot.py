 #!/usr/bin/env python3
import ai_engine
import os
import readline
import atexit

histfile = os.path.join(os.path.expanduser("~"), ".rs_history")
h_len = 0
try:
    readline.read_history_file(histfile)
    readline.set_history_length(1000)
except FileNotFoundError:
    open(histfile, 'wb').close()

def save(prev_h_len, histfile):
    new_h_len = readline.get_current_history_length()
    readline.set_history_length(1000)
    readline.append_history_file(new_h_len - prev_h_len, histfile)
    
atexit.register(save, h_len, histfile)

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

