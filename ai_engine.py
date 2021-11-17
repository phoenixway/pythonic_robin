 #!/usr/bin/env python3

from rules_engine import RulesEngine
from datetime import datetime

class AI:
    
    testRules = [
        {
            "trigger_type": "user_input", 
            "response_type": "func", 
            "input": "functest", 
            "func": lambda: str(1+1)
        }, 
        {
            "trigger_type": "user_input", 
            "response_type": "output", 
            "input": "test_testMode", 
            "output": "ok!"
        },
        {
            "trigger_type": "user_input", 
            "response_type": "output", 
            "input": "quit", 
            "output": "Have a nice day!"
        },    
        {
            "trigger_type": "user_input", 
            "response_type": "output", 
            "input": "", 
            "output": "Welcome!"
        },
        {
            "trigger_type": "mark and user_input", 
            "response_type": "ai_answer", 
            "mark": "testmark",
            "input": "whatsup", 
            "output": "generating answers for u"
        }
        ]

    def __init__(self) -> None:
        self.rulesEngine = RulesEngine()
        self._testingMode = False

    def get_isTesting(self):
        return self._testingMode

    def set_isTesting(self, value):
        self._testingMode = value
        if value:
            self.rulesEngine.rules = [*self.rulesEngine.rules, *AI.testRules]
        else:
            self.rulesEngine.rules = {item for item in self.rulesEngine.rules if item not in AI.testRules}

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
            elif rule.get("trigger_type", None) == "mark and user_input" and rule["input"] == msg and state["mark"] == rule["mark"]:
                answer = rule["output"]
                break
            elif rule.get("trigger_type", None) == "user_input" and rule["input"] == msg:
                if rule.get("response_type", None) == "output":
                    answer = rule["output"]
                elif rule.get("response_type", None) == "func":
                    answer = rule["func"]()
                break

        return status, answer, state