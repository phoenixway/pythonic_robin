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
        status, answer, state = self.ai.query("testScript", {})
        self.assertIsNot(status, 1)
        self.assertTrue(answer == "answer")
        status, answer, state = self.ai.query("test_testMode", {})
        self.assertIsNot(status, 1)
        self.assertTrue(answer == "ok!")
        status, answer, state = self.ai.query("functest", {})
        self.assertIsNot(status, 1)
        self.assertTrue(answer == "2")