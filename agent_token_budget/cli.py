"""Command line interface for agent-token-budget."""
from .budget import TokenBudgetManager

def main():
    mgr = TokenBudgetManager(max_tokens=10000, max_cost_usd=0.50)
    mgr.record_usage(2000, 500)
    print("Token budget manager active. Status:", mgr.status())

if __name__ == "__main__":
    main()
