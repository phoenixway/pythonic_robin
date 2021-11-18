 #!/usr/bin/env python3

from rules_engine import RulesEngine
from rules import In2Code_Rule, In2Out_Rule

class AI:
    
    testRules = [
        
        In2Code_Rule("functest", "str(1+1)"),
        In2Out_Rule("test_testMode", "ok!"),
        In2Out_Rule("quit", "Have a nice day!"),
        In2Out_Rule("", "Welcome!"),
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
            if rule.isTrue(msg):
                if isinstance(rule, In2Out_Rule) or isinstance(rule, In2Code_Rule):
                    answer = rule.activate()
                    break
            # elif rule.get("trigger_type", None) == "user_input" and rule["input"] == msg:
            #     if rule.get("response_type", None) == "output":
            #         answer = rule["output"]
            #     elif rule.get("response_type", None) == "func":
            #         answer = rule["func"]()
            #     break

        return status, answer, state