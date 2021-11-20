 #!/usr/bin/env python3
import ai_engine
import os, sys
import readline
import atexit
from termcolor import colored
from pathlib import Path

sys.path.insert(0, os.path.dirname(__file__))

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

current_dir = os.path.dirname(os.path.abspath(__file__))   # Can also use os.getcwd()
os.chdir(current_dir)

state = {}
state['status'] = 'default'
user_message = ""
ai = ai_engine.AI()
ai.isTesting = True
THIS_DIR = Path(__file__).parent
ai.rulesEngine.loadFromFile(THIS_DIR / "scripts/general.rules")
ai.rulesEngine.loadFromFile(THIS_DIR / "scripts/tools_script.rules")


while True:
    answer, state = ai.query(user_message, state)
    if answer != "" and answer != None:
        print(answer)  
    if state['status'] == 'quit':
        break
    user_message = input(colored(">> ", 'blue', attrs=['bold']))
print("Exiting..")

