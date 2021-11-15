 #!/usr/bin/env python3

import unittest
import ai_engine

class TestRules(unittest.TestCase):
    def setUp(self) -> None:
        self.ai = ai_engine.AI()
        self.ai.rulesEngine.loadFromFile("script1.rules")
        self.ai.isTesting = True
        return super().setUp()

    def test_1(self):
        status, answer, state = self.ai.query("hello", {})
        self.assertIsNot(status, 1)
        self.assertTrue(answer == "hey!")
        status, answer, state = self.ai.query("test", {})
        self.assertIsNot(status, 1)
        self.assertTrue(answer == "answer")