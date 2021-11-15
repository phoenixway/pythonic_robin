 #!/usr/bin/env python3

import unittest
import ai_engine

class TestRules(unittest.TestCase):
    def setUp(self) -> None:
        self.ai = ai_engine.AI()
        self.ai.rules_engine.loadFromFile("script1.rules")
        self.ai.isTesting = True
        return super().setUp()

    def test_1(self):
        
        status, answer, state = self.ai.get_answer("hello", {})
        self.assertIsNot(status, 1)
        self.assertTrue(answer == "hey!")