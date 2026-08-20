import os
import sys
import json
import csv
import argparse
import base64
import hashlib
from datetime import datetime

TOOL_NAME = "GHOST-Vault"
VERSION = "v1.0-PRO"

def banner():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    print(r"""
  ██████╗ ██╗  ██╗ ██████╗ ███████╗████████╗     ██╗   ██╗ █████╗ ██╗   ██╗████████╗
  ██╔════╝ ██║  ██║██╔═══██╗██╔════╝╚══██╔══╝     ██║   ██║██╔══██╗██║   ██║╚══██╔══╝
  ██║  ███╗███████║██║   ██║███████╗   ██║        ██║   ██║███████║██║   ██║   ██║   
  ██║   ██║██╔══██║██║   ██║╚════██║   ██║        ╚██╗ ██╔╝██╔══██║██║   ██║   ██║   
  ╚██████╔╝██║  ██║╚██████╔╝███████║   ██║         ╚████╔╝ ██║  ██║╚██████╔╝   ██║   
   ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝          ╚═══╝  ╚═╝  ╚═╝ ╚═════╝    ╚═╝   
    %s: Enterprise Secrets Intelligence & Credential Sanitizer (%s)
""" % (TOOL_NAME, VERSION))

def main():
    banner()
    parser = argparse.ArgumentParser(description=f"{TOOL_NAME} - Secure Credential & Secret Management Framework")
    parser.add_argument("--scan", help="Scan directory or file for hardcoded secrets")
    parser.add_argument("--hash", help="Hash a credential string securely")
    parser.add_argument("--json", default="vault_report.json", help="JSON report output")
    parser.add_argument("--csv", default="vault_report.csv", help="CSV report output")
    args = parser.parse_args()

    if args.hash:
        digest = hashlib.sha256(args.hash.encode()).hexdigest()
        print(f"[+] SHA256 Hash of provided string: {digest}")
        return

    target = args.scan
    if not target:
        target = input("[*] Enter target directory or file path to scan for secrets: ").strip()

    print(f"\n[+] Executing empirical secret sanitization and audit for: {target}")
    findings = []

    if os.path.exists(target):
        if os.path.isfile(target):
            paths = [target]
        else:
            paths = []
            for root, _, files in os.walk(target):
                for file in files:
                    paths.append(os.path.join(root, file))

        for p in paths:
            try:
                with open(p, 'r', encoding='utf-8', errors='ignore') as f:
                    lines = f.readlines()
                for idx, line in enumerate(lines, 1):
                    lower = line.lower()
                    if any(k in lower for k in ["api_key", "password", "secret", "private_key", "bearer", "token"]):
                        findings.append({
                            "file": p,
                            "line": idx,
                            "match_snippet": line.strip()[:60] + "...",
                            "timestamp": datetime.utcnow().isoformat()
                        })
            except Exception:
                pass
    else:
        findings.append({
            "target": target,
            "status": "Target path not found",
            "timestamp": datetime.utcnow().isoformat()
        })

    with open(args.json, 'w', encoding='utf-8') as jf:
        json.dump(findings, jf, indent=4)
    print(f"[+] Vault JSON Report saved to: {args.json}")

    with open(args.csv, 'w', newline='', encoding='utf-8') as cf:
        writer = csv.DictWriter(cf, fieldnames=["file", "line", "match_snippet", "timestamp", "target", "status"])
        writer.writeheader()
        for row in findings:
            writer.writerow({k: row.get(k, "") for k in ["file", "line", "match_snippet", "timestamp", "target", "status"]})
    print(f"[+] Vault CSV Report saved to: {args.csv}")

if __name__ == "__main__":
    main()
