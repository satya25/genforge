"""
============================================================
 File: test_agent.py
 Project: Agentic Hello World
============================================================

Purpose:
--------
Provides a minimal unit test for HelloAgent.
"""

import unittest
from src.agents.hello_agent import HelloAgent


class TestHelloAgent(unittest.TestCase):
    """
    Unit tests for HelloAgent class.
    """

    def test_greet(self):
        agent = HelloAgent()
        self.assertEqual(agent.greet(), "Hello from HelloAgent!")


if __name__ == "__main__":
    unittest.main()
