 #!/usr/bin/env python

class In2Out_Rule():
    def __init__(self, input, output) -> None:
        self.input = input
        self.output = output
    def activate(self):
        return self.output
    def isTrue(self, message):
        if message == self.input:
            return True

class In2Code_Rule():
    def __init__(self, input, code) -> None:
        self.input = input
        self.code = code
    def activate(self):
        return eval(self.code)
    def isTrue(self, message):
        if message == self.input:
            return True