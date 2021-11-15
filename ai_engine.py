 #!/usr/bin/env python3

from rules_engine import RulesEngine
from datetime import datetime

class AI:
    
    def __init__(self) -> None:
        self.rulesEngine = RulesEngine()
        self._testingMode = False

    def get_isTesting(self):
        return self._testingMode

    def set_isTesting(self, value):
        self._testingMode = value
        if value:
            self.rulesEngine.rules.append({
                "type": "answer", 
                "input": "hello", 
                "output": "hey!"
            })
            self.rulesEngine.rules.append({
                "type": "func", 
                "input": "time", 
                "func": lambda: datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            })

            self.rulesEngine.rules.append({
                "trigger_type": "user_input", 
                "response_type": "func", 
                "input": "time2", 
                "func": lambda: datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            })

            self.rulesEngine.rules.append({
                "trigger_type": "mark and user_input", 
                "response_type": "ai_answer", 
                "mark": "testmark",
                "input": "whatsup", 
                "output": "generating answers for u"
            })

            self.rulesEngine.rules.append({"type": "answer", "input": "quit", "output": "Have a nice day!"})
            self.rulesEngine.rules.append({"type": "answer", "input": "", "output": "Welcome!"})
            self.rulesEngine.rules.append({"type": "answer", "input": "what?", "output": "dont know"})
        
    isTesting = property(get_isTesting, set_isTesting)

    def query(self, msg, state):
        answer = "Don't know what to say."
        status = 1 if msg == "quit" else 0 

        for rule in self.rulesEngine.rules:
            if "type" in rule and rule["type"] == "answer" and rule["input"] == msg:
                answer = rule["output"]
                break
            elif "type" in rule and rule["type"] == "func" and rule["input"] == msg:
                answer = rule["func"]()
                break
            elif "trigger type" in rule and rule["trigger_type"] == "mark and user_input" and rule["input"] == msg and state["mark"] == rule["mark"]:
                answer = rule["output"]
                break

        return status, answer, state