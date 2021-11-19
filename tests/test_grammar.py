 #!/usr/bin/env python3

import unittest
from rs_engine import RulesEngine

class TestGrammar(unittest.TestCase):
    def setUp(self) -> None:
        self.rules_engine = RulesEngine()
        return super().setUp()

    def test_in2out(self):
        test_data = '''
        bla>>>bla2
        '''
        parseTree = self.rules_engine.rs_parser.parseString(test_data)
        item = parseTree[0]
        self.assertTrue('in2out' in item)
        self.assertEqual(item['in2out'][0], "bla")
        self.assertEqual(item['in2out'][1], "bla2")

    def test_in2out1(self):
        test_data = '''
        bla >>> bla2
        '''
        parseTree = self.rules_engine.rs_parser.parseString(test_data)
        item = parseTree[0]
        self.assertTrue('in2out' in item)
        self.assertEqual(item['in2out'][0], "bla")
        self.assertEqual(item['in2out'][1], "bla2")

    def test_in2out2(self):
        test_data = '''
        bla3 bla4 >>> bla2 blat5 7
        '''
        parseTree = self.rules_engine.rs_parser.parseString(test_data)
        item = parseTree[0]
        self.assertTrue('in2out' in item)
        self.assertEqual(item['in2out'][0], "bla3 bla4")
        self.assertEqual(item['in2out'][1], "bla2 blat5 7")

    def test_multyline(self):
        test_data = '''
        bla>>>bla2
        bla3 text >>> bla4 text 2
        #comment it
        '''
        parseTree = self.rules_engine.rs_parser.parseString(test_data)
        self.assertEqual(len(parseTree), 3)
        item = parseTree[0]
        self.assertTrue('in2out' in item)
        self.assertEqual(item['in2out'][0], "bla")
        self.assertEqual(item['in2out'][1], "bla2")
        item = parseTree[1]
        self.assertTrue('in2out' in item)
        self.assertEqual(item['in2out'][0], "bla3 text")
        self.assertEqual(item['in2out'][1], "bla4 text 2")
        item = parseTree[2]
        self.assertTrue('comment' in item)
        self.assertEqual(item['comment'][0], "comment it")

    def test_code1(self):
        test_data = '''
        bla>>>bla2
        bla3 text >>> bla4 text 2
        #comment it
        func >>> { 
            code5('test')
        }
        '''
        parseTree = self.rules_engine.rs_parser.parseString(test_data)
        item = parseTree[3]
        self.assertTrue('in2code' in item)
        self.assertEqual(item['code'][0], "code5('test')")
        #FIXME
        self.assertEqual(item['in2code'][0], "func")

    def test_code2(self):
        test_data = '''
        bla>>>bla2
        bla3 text >>> bla4 text 2
        #comment it
        func >>>
        { 
            code5('test')
        }
        '''
        parseTree = self.rules_engine.rs_parser.parseString(test_data)
        item = parseTree[3]
        self.assertTrue('in2code' in item)
        self.assertEqual(item['code'][0], "code5('test')")
        self.assertEqual(item['in2code'][0], "func")

    def test_code3(self):
        test_data = '''
        bla>>>bla2
        bla3 text >>> bla4 text 2
        #comment it
        func >>> {code5('test')
        }
        '''
        parseTree = self.rules_engine.rs_parser.parseString(test_data)
        item = parseTree[3]
        self.assertTrue('in2code' in item)
        self.assertEqual(item['code'][0], "code5('test')")
        self.assertEqual(item['in2code'][0], "func")

    def test_code4(self):
        test_data = '''
        bla>>>bla2
        bla3 text >>> bla4 text 2
        #comment it
        func >>> { code5('test') }
        '''
        parseTree = self.rules_engine.rs_parser.parseString(test_data)
        item = parseTree[3]
        self.assertTrue('in2code' in item)
        #FIXME
        self.assertEqual(item['code'][0], "code5('test') ")
        self.assertEqual(item['in2code'][0], "func")

    def test_code5(self):
        test_data = '''
        bla>>>bla2
        bla3 text >>> bla4 text 2
        #comment it
        func >>> { 
            code5('test')
        }
        '''
        parseTree = self.rules_engine.rs_parser.parseString(test_data)
        item = parseTree[3]
        self.assertTrue('in2code' in item)
        self.assertEqual(item['code'][0], "code5('test')")
        self.assertEqual(item['in2code'][0], "func")

    def test_code6(self):
        test_data = '''
        bla>>>bla2
        bla3 text >>> bla4 text 2
        #comment it
        func >>> { 
            code5('test')
            code6('bla')
        }
        '''
        parseTree = self.rules_engine.rs_parser.parseString(test_data)
        item = parseTree[3]
        self.assertTrue('in2code' in item)
        self.assertEqual(item['code'][0], "code5('test')")
        self.assertEqual(item['in2code'][0], "func")
    
    def test_code_js_inline_multiple_words(self):
        test_data = '''inpt >>> jscode fuck shit end_jscode'''
        parseTree = self.rules_engine.rs_parser.parseString(test_data)
        item = parseTree[0]
        self.assertTrue('in2jscode' in item)
        self.assertEqual(item['in2jscode'][0], "inpt")
        self.assertEqual(item['in2jscode'][1], "fuck")

    def test_code7_1(self):
        test_data = '''
        inpt >>> jscode fuck shit end_jscode
        inpt1 >>> jscode fuck1 shit1 end_jscode

        '''
        parseTree = self.rules_engine.rs_parser.parseString(test_data)
        item = parseTree[0]
        self.assertTrue('in2jscode' in item)
        self.assertEqual(item['in2jscode'][0], "inpt")
        self.assertEqual(item['in2jscode'][1], "fuck")
        item = parseTree[1]
        self.assertTrue('in2jscode' in item)
        self.assertEqual(item['in2jscode'][0], "inpt1")
        self.assertEqual(item['in2jscode'][1], "fuck1")

    def test_code_js_with_eol(self):
        test_data = '''
        inpt >>> jscode 
        fuck 
        shit end_jscode
        inpt1 >>> jscode 
            fuck1 
            shit1 
        end_jscode

        '''
        parseTree = self.rules_engine.rs_parser.parseString(test_data)
        item = parseTree[0]
        self.assertTrue('in2jscode' in item)
        self.assertEqual(item['in2jscode'][0], "inpt")
        self.assertEqual(item['in2jscode'][1], "fuck")
        item = parseTree[1]
        self.assertTrue('in2jscode' in item)
        self.assertEqual(item['in2jscode'][0], "inpt1")
        self.assertEqual(item['in2jscode'][1], "fuck1")

    def test_code_js_with_eol2(self):
        test_data = '''
        inpt1 >>> jscode 
            fuck1 
            shit1 
        end_jscode

        '''
        parseTree = self.rules_engine.rs_parser.parseString(test_data)
        item = parseTree[0]
        self.assertTrue('in2jscode' in item)
        self.assertEqual(item['in2jscode'][0], "inpt1")
        self.assertEqual(item['in2jscode'][1], "fuck1")

    def test_code7_3(self):
        test_data = '''inpt >>> jscode fuck shit end_jscode'''
        parseTree = self.rules_engine.rs_parser.parseString(test_data)
        item = parseTree[0]
        self.assertTrue('in2jscode' in item)
        self.assertEqual(item['in2jscode'][0], "inpt")
        self.assertEqual(item['in2jscode'][1], "fuck")


    def test_code8(self):
        test_data = '''
        inpt >>> jscode 
        fuck 
        shit
        end_jscode
        '''
        parseTree = self.rules_engine.rs_parser.parseString(test_data)
        item = parseTree[0]
        self.assertTrue('in2jscode' in item)
        self.assertEqual(item['in2jscode'][0], "inpt")
        self.assertEqual(item['in2jscode'][1], "fuck")

    def test_code9(self):
        test_data = '''
        inpt >>> jscode 
            fuck fuck2
            shit shit2
        end_jscode
        '''
        parseTree = self.rules_engine.rs_parser.parseString(test_data)
        item = parseTree[0]
        self.assertTrue('in2jscode' in item)
        self.assertEqual(item['in2jscode'][0], "inpt")
        self.assertEqual(item['in2jscode'][1], "fuck")

    def test_code10(self):
        test_data = '''
        js_func >>> jscode 
            var x = {company: 'Sqreen'}; 
            x.company;
            x.company
        end_jscode
        '''
        parseTree = self.rules_engine.rs_parser.parseString(test_data)
        item = parseTree[0]
        self.assertTrue('in2jscode' in item)
        self.assertEqual(item['in2jscode'][0], "js_func")
        s = ""
        for i in item['jscode']:
            s = s + i + " "
        self.assertEqual(s, "var x = {company: 'Sqreen'}; x.company; x.company ")

    def test_code11(self):
        test_data = '''
        hello >>> jscode
            greatings = ['hey!', 'hello, great warrior!', 'sholom, eternal champion!'] ;
            i = Math.floor(Math.random() * 3) ;
            greatings[i]
        end_jscode
        '''
        parseTree = self.rules_engine.rs_parser.parseString(test_data)
        item = parseTree[0]
        self.assertTrue('in2jscode' in item)
 