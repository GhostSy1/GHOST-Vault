# GHOST-Vault

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **Enterprise Secrets Intelligence & Credential Sanitizer**  
> Developed by Abdulaziz (Ghost-SY1).

---

## Overview
**GHOST-Vault** is a robust, open-source command-line framework engineered to solve a pervasive problem among penetration testers, security researchers, and software engineers: **accidental exposure of hardcoded secrets, API keys, private keys, and sensitive credentials in source code repositories**.

---

## Key Features
- **Deep Recursive Scanning**: Inspects directories, configuration files, and source code for high-entropy tokens and credential keywords.
- **Empirical Evidence Extraction**: Logs exact file paths, line numbers, and truncated match snippets without storing raw secrets in insecure logs.
- **Structured Reporting**: Exports findings directly to standardized JSON and CSV formats for audit trails and CI/CD integration.
- **Secure CLI Workflow**: Direct terminal execution with clean output formatting.

---

## Installation & Usage
```bash
git clone https://github.com/GhostSy1/GHOST-Vault.git
cd GHOST-Vault
pip install -r requirements.txt
python3 main.py --scan /path/to/project
```

---

## License
Distributed under the MIT License. See `LICENSE` for more information.
