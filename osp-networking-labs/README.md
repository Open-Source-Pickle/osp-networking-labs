# OSP Networking Labs — Wi‑Fi • VPN • Firewalls • Diagnostics

Make networking policy‑as‑code. Author YAML, validate, convert to JSON, push via APIs. Includes diagnostics and monitoring configs.

Quick Start:
1) python3 -m venv .venv && source .venv/bin/activate
2) pip install -r requirements.txt
3) python diagnostics/network_diagnostics.py
4) python firewall/apply_rules.py --rules firewall/firewall-rules.yaml
