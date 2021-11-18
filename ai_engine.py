 #!/usr/bin/env python3

from rs_engine import RulesEngine
from rules import *
from padatious import IntentContainer

class AI:
    
    def quitStatus(state):
        state['status']='quit'
        return state

    testRules = [
        
        In2Code_Rule("functest", "str(1+1)"),
        In2Out_Rule("test_testMode", "ok!"),
        In2OutAndState_Rule("goodbye", "Have a nice day!", state_change=quitStatus ),
        In2Out_Rule("", "Welcome!")
        # ,
        # {
        #     "trigger_type": "mark and user_input", 
        #     "response_type": "ai_answer", 
        #     "mark": "testmark",
        #     "input": "whatsup", 
        #     "output": "generating answers for u"
        # }
        ]

    def __init__(self) -> None:
        self.rulesEngine = RulesEngine()
        self._testingMode = False
        self.container = IntentContainer('intent_cache')
        self.container.load_file('hello', 'intents/hello.intent')
        self.container.load_file('goodbye', 'intents/goodbye.intent')
        self.container.load_file('cursing', 'intents/cursing.intent')
        self.container.load_file('time', 'intents/time.intent')
        self.container.load_file('thank u', 'intents/thanks.intent')
        self.container.train()

    def get_isTesting(self):
        return self._testingMode

    def set_isTesting(self, value):
        self._testingMode = value
        if value:
            self.rulesEngine.rules = [*self.rulesEngine.rules, *AI.testRules]
        else:
            self.rulesEngine.rules = {item for item in self.rulesEngine.rules if item not in AI.testRules}

    isTesting = property(get_isTesting, set_isTesting)

    def findRule(self, msg, state={}):
        r = None
        for rule in self.rulesEngine.rules:
            if rule.isTrue(msg):
                if isinstance(rule, In2Out_Rule) or isinstance(rule, In2Code_Rule):
                    r = rule
                    break
        if r is None:
            data = self.container.calc_intent(msg)
            r = self.findRule(data.name) if data.conf > 0.6 else None
        return r

    def query(self, msg, state):
        answer = "Don't know what to say." 

        rule = self.findRule(msg)
        if rule != None:
            rule.updateState(state)
            answer, state = rule.activate()
            # elif rule.get("trigger_type", None) == "user_input" and rule["input"] == msg:
            #     if rule.get("response_type", None) == "output":
            #         answer = rule["output"]
            #     elif rule.get("response_type", None) == "func":
            #         answer = rule["func"]()
            #     break

        return answer, state