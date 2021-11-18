 #!/usr/bin/env python

class In2Out_Rule():
    def __init__(self, input, output, state={}) -> None:
        self.input = input
        self.output = output
        self.state = state
    def updateState(self, state):
        self.state = state
    def activate(self):
        return self.output, self.state
    def isTrue(self, message):
        if message == self.input:
            return True

class In2OutAndState_Rule(In2Out_Rule):
    def __init__(self, input, output, state={}, state_change=None) -> None:
        self.state_change = state_change
        super().__init__(input, output)
    def updateState(self, state):
        self.state = state
    def activate(self):
        self.state = self.state_change(self.state)
        return self.output, self.state

class In2Code_Rule():
    def __init__(self, input, code, state={}) -> None:
        self.input = input
        self.code = code
    def updateState(self, state):
        self.state = state
    def activate(self):
        eval("exec('from datetime import datetime')")
        return eval(self.code), self.state
    def isTrue(self, message):
        if message == self.input:
            return True