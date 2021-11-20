 #!/usr/bin/env python3
import unittest
import ai_engine
from pathlib import Path
from pprint import pprint
THIS_DIR = Path(__file__).parent

class TestScripts(unittest.TestCase):
    def setUp(self) -> None:
        self.ai = ai_engine.AI()
        self.ai.rulesEngine.loadFromFile(THIS_DIR.parent / "scripts/test_script.rules")
        self.ai.isTesting = True
        return super().setUp()

    def test_indent_block(self):
        test_data = '''
            bla>>>bla2
            bla3 text >>> bla4 text 2
                b5 >>> b6
                    b7 >>> b8
                    b9 >>> b10
        '''
        parseTree =self.ai.rulesEngine.rs_parser.parseString(test_data)
        item = parseTree[0]
        pprint(item)
        print(item.dump())
        pass
        #self.assertTrue('in2code' in item)
        #self.assertEqual(item['code'][0], "code5('test')")
        #FIXME
        #self.assertEqual(item['in2code'][0], "func")