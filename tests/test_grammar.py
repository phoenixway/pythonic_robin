 #!/usr/bin/env python3

import unittest
import rs_parser

class TestGrammar(unittest.TestCase):
    def setUp(self) -> None:
        self.grammar = rs_parser.RobinScriptGrammar()
        return super().setUp()

    def test_in2out(self):
        test_data = '''
        bla=>bla2
        '''
        parseTree = self.grammar.module_body.parseString(test_data)
        item = parseTree[0]
        self.assertTrue('in2out' in item)
        self.assertEqual(item['in2out'][0], "bla")
        self.assertEqual(item['in2out'][1], "bla2")

    def test_multyline(self):
        test_data = '''
        bla=>bla2
        bla3 text => bla4 text 2
        #comment it
        '''
        parseTree = self.grammar.module_body.parseString(test_data)
        item = parseTree[0]
        self.assertTrue('in2out' in item)
        self.assertEqual(item['in2out'][0], "bla")
        self.assertEqual(item['in2out'][1], "bla2")
        item = parseTree[1]
        self.assertTrue('in2out' in item)
        self.assertEqual(item['in2out'][0], "bla3 text ")
        self.assertEqual(item['in2out'][1], "bla4 text 2")
        item = parseTree[2]
        self.assertTrue('comment' in item)
        self.assertEqual(item['comment'][0], "comment it")

    def test_code1(self):
        test_data = '''
        bla=>bla2
        bla3 text => bla4 text 2
        #comment it
        func => { 
            code5('test')
        }
        '''
        parseTree = self.grammar.module_body.parseString(test_data)
        item = parseTree[3]
        self.assertTrue('in2code' in item)
        self.assertEqual(item['code'][0], "code5('test')")
        #FIXME
        self.assertEqual(item['in2code'][0], "func ")

    def test_code2(self):
        test_data = '''
        bla=>bla2
        bla3 text => bla4 text 2
        #comment it
        func => 
        { 
            code5('test')
        }
        '''
        parseTree = self.grammar.module_body.parseString(test_data)
        item = parseTree[3]
        self.assertTrue('in2code' in item)
        self.assertEqual(item['code'][0], "code5('test')")
        self.assertEqual(item['in2code'][0], "func ")

    def test_code3(self):
        test_data = '''
        bla=>bla2
        bla3 text => bla4 text 2
        #comment it
        func => {code5('test')
        }
        '''
        parseTree = self.grammar.module_body.parseString(test_data)
        item = parseTree[3]
        self.assertTrue('in2code' in item)
        self.assertEqual(item['code'][0], "code5('test')")
        self.assertEqual(item['in2code'][0], "func ")

    def test_code4(self):
        test_data = '''
        bla=>bla2
        bla3 text => bla4 text 2
        #comment it
        func => { code5('test') }
        '''
        parseTree = self.grammar.module_body.parseString(test_data)
        item = parseTree[3]
        self.assertTrue('in2code' in item)
        #FIXME
        self.assertEqual(item['code'][0], "code5('test') ")
        self.assertEqual(item['in2code'][0], "func ")

    def test_code5(self):
        test_data = '''
        bla=>bla2
        bla3 text => bla4 text 2
        #comment it
        func => { 
            code5('test')
        }
        '''
        parseTree = self.grammar.module_body.parseString(test_data)
        item = parseTree[3]
        self.assertTrue('in2code' in item)
        self.assertEqual(item['code'][0], "code5('test')")
        self.assertEqual(item['in2code'][0], "func ")