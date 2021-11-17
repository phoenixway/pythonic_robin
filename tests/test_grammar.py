 #!/usr/bin/env python3

import unittest
import rs_parser

class TestGrammar(unittest.TestCase):
    def setUp(self) -> None:
        self.grammar = rs_parser.RobinScriptGrammar()
        return super().setUp()

    def test_1(self):
        test_data = '''
        bla=>bla2
        bla3 text => bla4 text 2
        #comment it
        '''
        parseTree = self.grammar.module_body.parseString(test_data)
        for item in parseTree:
            print("Is {} a in2out? {}".format(item, 'in2out' in item))
            if 'in2out' in item:
                print("Content is: {}".format(item['in2out']))
                print("Input: {}, output: {}".format(item['in2out'][0], item['in2out'][1]))
        print(parseTree)
        #parseTree.pprint()
        print(parseTree)