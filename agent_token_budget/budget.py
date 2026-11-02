"""Token budget manager and tracker."""
from typing import Dict, Any, List

class TokenBudgetManager:
    def __init__(self, max_tokens: int = 100000, max_cost_usd: float = 2.0):
        self.max_tokens = max_tokens
        self.max_cost_usd = max_cost_usd
        self.used_tokens = 0
        self.estimated_cost = 0.0
        self.turn_history: List[Dict[str, Any]] = []

    def record_usage(self, prompt_tokens: int, completion_tokens: int, cost_per_1k: float = 0.002) -> bool:
        turn_tokens = prompt_tokens + completion_tokens
        turn_cost = (turn_tokens / 1000.0) * cost_per_1k
        self.used_tokens += turn_tokens
        self.estimated_cost += turn_cost
        self.turn_history.append({
            "tokens": turn_tokens,
            "cost": turn_cost,
            "cumulative_tokens": self.used_tokens
        })
        return self.is_within_budget()

    def is_within_budget(self) -> bool:
        return self.used_tokens < self.max_tokens and self.estimated_cost < self.max_cost_usd

    def remaining_tokens(self) -> int:
        return max(0, self.max_tokens - self.used_tokens)

    def status(self) -> Dict[str, Any]:
        pct_used = (self.used_tokens / self.max_tokens * 100.0) if self.max_tokens > 0 else 100.0
        return {
            "used_tokens": self.used_tokens,
            "max_tokens": self.max_tokens,
            "remaining_tokens": self.remaining_tokens(),
            "pct_used": round(pct_used, 2),
            "estimated_cost_usd": round(self.estimated_cost, 4),
            "is_exhausted": not self.is_within_budget()
        }
