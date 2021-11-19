 #!/usr/bin/env python3
import sys, os
sys.path.insert(0, os.path.abspath('..'))

import unittest
import ai_engine
from pathlib import Path
THIS_DIR = Path(__file__).parent

class TestRules(unittest.TestCase):
    def setUp(self) -> None:
        self.ai = ai_engine.AI()
        self.ai.rulesEngine.loadFromFile(THIS_DIR.parent / "scripts/test_script.rules")
        self.ai.isTesting = True
        return super().setUp()

    def test_fake(self):
        ...