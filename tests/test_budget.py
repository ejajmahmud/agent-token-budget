"""Unit tests for TokenBudgetManager."""
import unittest
from agent_token_budget.budget import TokenBudgetManager

class TestTokenBudget(unittest.TestCase):
    def test_budget_consumption(self):
        mgr = TokenBudgetManager(max_tokens=5000, max_cost_usd=1.0)
        ok = mgr.record_usage(1000, 500)
        self.assertTrue(ok)
        self.assertEqual(mgr.remaining_tokens(), 3500)
        self.assertEqual(mgr.status()["pct_used"], 30.0)

    def test_budget_exhaustion(self):
        mgr = TokenBudgetManager(max_tokens=1000, max_cost_usd=1.0)
        mgr.record_usage(800, 300)
        self.assertFalse(mgr.is_within_budget())
        self.assertEqual(mgr.remaining_tokens(), 0)

if __name__ == "__main__":
    unittest.main()
