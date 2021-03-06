 #!/usr/bin/env python3

from rs_engine import RulesEngine
from rules import *
from padatious import IntentContainer
from tools.quotes import getQuote
from pathlib import Path
import pprint

THIS_DIR = Path(__file__).parent

class AI:
    
    def __init__(self) -> None:
        self.rulesEngine = RulesEngine()
        self._testingMode = False
        self.initIntents()

    def initIntents(self):
        try:
            r = IntentContainer('intent_cache')
            r.load_file('hello', THIS_DIR / 'intents/hello.intent')
            r.load_file('goodbye', THIS_DIR / 'intents/goodbye.intent')
            r.load_file('cursing', THIS_DIR / 'intents/cursing.intent')
            r.load_file('time', THIS_DIR / 'intents/time.intent')
            r.load_file('thank u', THIS_DIR / 'intents/thanks.intent')
            r.load_file('inspire', THIS_DIR / 'intents/inspire.intent')
            r.train()
            self.intent_recognizer = r
        except Exception:
            print('Intents error.')

    def quitStatus(state):
        state['status']='quit'
        return state

    testRules = [
        In2Code_Rule("functest", "str(1+1)"),
        In2Out_Rule("test_testMode", "ok!"),
        In2OutAndState_Rule("goodbye", "Have a nice day!", state_change=quitStatus ),
        In2Out_Rule("", "Welcome!\n" + getQuote())
    ]

    def getIsTesting(self):
        return self._testingMode

    def setIsTesting(self, value):
        self._testingMode = value
        if value:
            self.rulesEngine.rules = [*self.rulesEngine.rules, *AI.testRules]
            self.rulesEngine.loadFromFile(THIS_DIR / "scripts/test_script.rules")

        else:
            self.rulesEngine.rules = {item for item in self.rulesEngine.rules if item not in AI.testRules}
        pass

    isTesting = property(getIsTesting, setIsTesting)

    def isInRules(self, msg): 
        r = None
        for rule in self.rulesEngine.rules:
            if rule.isTrue(msg):
                if isinstance(rule, In2Out_Rule) or isinstance(rule, In2Code_Rule) or isinstance(rule, In2JSCode_Rule):
                    r = rule
                    break
        return r

    def findRule(self, msg, state={}):
        r = self.isInRules(msg)
        if r is None:
            data = self.intent_recognizer.calc_intent(msg)
            r = self.isInRules(data.name) if data.conf > 0.5 else None
        return r

    def query(self, msg, state):
        answer = "Don't know what to say." 
        rule = self.findRule(msg)
        if rule != None:
            rule.updateState(state)
            answer, state = rule.activate()
        return answer, state