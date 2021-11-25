 #!/usr/bin/env python
 
from py_mini_racer import py_mini_racer

class In2Out_Rule():
    def __init__(self, input=None, output=None, state={}, state_change=None) -> None:
        self.input = input
        self.output = output
        self.state_change = state_change
        #super().__init__(input, output)
    def __repr__(self):
        return "\nIn2out rule >> (\n\tin: '{}', \n\tout: '{}' \n)".format(self.input, self.output)
    def updateState(self, state):
        self.state = state
    def activate(self):
        return self.output, self.state
    def isTrue(self, message):
        if message == self.input:
            return True
            
class In2Nested_Rule(In2Out_Rule):
    def __init__(self, input=None, output=None, state={}, state_change=None) -> None:
        self.state_change = state_change
        self.nested = None
        super().__init__(input, output)
    def __repr__(self):
        return "\nIn2nested rule >> (\n\tin: '{}', \n\tout: '{}', \n\tnested: '{}' \n)".format(self.input, self.output, self.nested)
    def updateState(self, state):
        self.state = state
    def activate(self):
        return self.output, self.state
    def isTrue(self, message):
        if message == self.input:
            return True



class In2OutAndState_Rule(In2Out_Rule):
    def __init__(self, input=None, output=None, state={}, state_change=None) -> None:
        super().__init__(input, output, state_change = state_change)
    def updateState(self, state):
        self.state = state
    def activate(self):
        if self.state_change is not None:
            self.state = self.state_change(self.state)
        return self.output, self.state

class In2Code_Rule():
    def __init__(self, input, code, state={}) -> None:
        self.input = input
        self.code = code
    def updateState(self, state):
        self.state = state
    def activate(self):
        result = None
        if isinstance(self.code, list):
            for c in self.code:
                result = eval(c)
        else:
            result = eval(self.code)
        return result, self.state
    def isTrue(self, message):
        if message == self.input:
            return True

class In2JSCode_Rule():
    def __init__(self, input, code, state={}) -> None:
        self.input = input
        self.code = code
    def updateState(self, state):
        self.state = state
    def activate(self):
        result = None
        ctx = py_mini_racer.MiniRacer()
        if isinstance(self.code, list):
            for c in self.code:
                result = ctx.eval(c)
        else:
            result = ctx.eval(self.code)
        return result, self.state
    def isTrue(self, message):
        if message == self.input:
            return True