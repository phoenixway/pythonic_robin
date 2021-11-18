 #!/usr/bin/env python3

import unittest
import ai_engine

class TestRulesEngine(unittest.TestCase):
    def setUp(self) -> None:
        self.ai = ai_engine.AI()
        self.ai.rulesEngine.loadFromFile("script1.rules")
        self.ai.isTesting = True
        return super().setUp()

    def test_1(self):
        answer, state  = self.ai.query("testScript", {})
        if 'status' in state:
            self.assertIsNot(state["status"], "quit")
        self.assertTrue(answer == "answer")
        # status, answer, state = self.ai.query("test_testMode", {})
        # self.assertIsNot(status, 1)
        # self.assertTrue(answer == "ok!")
        # status, answer, state = self.ai.query("functest", {})
        # self.assertIsNot(status, 1)
        # self.assertTrue(answer == "2")
