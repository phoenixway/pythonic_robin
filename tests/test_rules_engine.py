 #!/usr/bin/env python3

import unittest
import ai_engine

class TestRules(unittest.TestCase):
    def test_1(self):
        ai = ai_engine.AI()
        status, answer, state = ai.get_answer("hello", {})
        self.assertIsNot(status, 1)
        self.assertTrue(answer == "hey!")