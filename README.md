# GHOST-Vault

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **Enterprise Secrets Sanitizer & Secure Storage Engine**  
> Developed by Abdulaziz (Ghost-SY1).

---

## Table of Contents
1. [Overview & Purpose](#overview--purpose)
2. [Core Architecture](#core-architecture)
3. [Usage & CLI Reference](#usage-guide--cli-reference)
4. [License](#license)

---

## Overview & Purpose
**GHOST-Vault** is an enterprise-grade utility designed to scan codebases, configuration files, and evidentiary drops for exposed API keys, private keys, passwords, and tokens, sanitizing them before reporting or storage.

---

## Core Architecture
- **Regex Sanitization Engine**: Matches standard high-entropy secrets and credentials.
- **SHA-256 Fingerprinting**: Tags sanitized outputs with cryptographic integrity hashes.

---

## Usage
```bash
python3 main.py --scan /path/to/project --out sanitized.json
```
