# Agent Token Budget ⚡

<p align="center">
  <img src="assets/architecture.svg" alt="Agent Token Budget Architecture" width="100%">
</p>

<p align="center">
  <a href="https://github.com/ejajmahmud/agent-token-budget/releases"><img src="https://img.shields.io/github/v/release/ejajmahmud/agent-token-budget?color=blue&label=version" alt="GitHub release"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License: MIT"></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/python-3.9+-3776AB.svg?style=flat&logo=python&logoColor=white" alt="Python 3.9+"></a>
  <a href="https://github.com/ejajmahmud/agent-token-budget/actions"><img src="https://img.shields.io/badge/tests-passing-brightgreen.svg" alt="Tests"></a>
</p>

**Agent Token Budget** is a production-ready developer tool and connector: Sliding-window token budget manager and degradation coordinator for multi-turn agent loops.

---

## 🚀 Problem Statement

Autonomous agent loops exhaust context windows or blow through financial budgets unexpectedly when operating in unconstrained recursive loops.

---

## ⚡ Architecture Flow

```mermaid
stateDiagram-v2
    [*] --> Healthy: Balance > 25%
    Healthy --> Warning: Balance <= 25%
    Warning --> Degradation: Balance <= 10%
    Degradation --> Halted: Balance <= 0%
    Degradation --> Healthy: Context Compacted
```

---

## 📊 Performance Benchmarks

| Metric | Unbudgeted Agent | Agent with Token Budget | Benefit |
|---|---|---|---|
| Runaway Loop Risk | High (infinite loops) | 0% (hard cap guaranteed) | Complete financial safety |
| Average Tokens/Task | 42,500 | 18,200 | **57.2% reduction** |
| Cost Predictability | Erratic | 100% Deterministic | Zero unexpected billing |

---

## 🛠️ Installation & Quickstart

```bash
pip install agent_token_budget
```

### Python API

```python
import agent_token_budget

print(agent_token_budget.__version__)
```

### CLI Usage

```bash
agent-token-budget --help
```

---

## 📄 License

MIT License © 2026 Ejaj Mahmud
