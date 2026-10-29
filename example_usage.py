# -*- coding: utf-8 -*-
from client import GenParkAgentMCPToolPermissionLeastPrivilegeAuditor

def main():
    auditor = GenParkAgentMCPToolPermissionLeastPrivilegeAuditor(max_allowed_blast_radius=2.0)
    print("=== GenPark Agent MCP Least-Privilege Auditor ===")

    # Scenario 1: Dangerous broad-permission manifest
    dangerous_suite = [
        {"name": "web_scraper", "capabilities": ["network_get"]},
        {"name": "file_saver", "capabilities": ["fs_write"], "parameters": {"properties": {"filepath": {}}}},
        {"name": "system_exec", "capabilities": ["exec"], "parameters": {"properties": {"command": {}}}}
    ]
    res1 = auditor.audit_tool_manifest(dangerous_suite)
    print(f"Dangerous Suite: Compliant={res1['least_privilege_compliant']}, BlastRadius={res1['aggregate_blast_radius']}")
    for esc in res1["escalation_vectors"]:
        print(f"  [ALERT] {esc['vector']}: {esc['detail']}")

    # Scenario 2: Hardened least-privilege manifest
    hardened_suite = [
        {"name": "lookup_stock_ticker", "capabilities": ["db_read"]},
        {"name": "compute_moving_average", "capabilities": ["pure_calc"]}
    ]
    res2 = auditor.audit_tool_manifest(hardened_suite)
    print()
    print(f"Hardened Suite: Compliant={res2['least_privilege_compliant']}, BlastRadius={res2['aggregate_blast_radius']}")

if __name__ == "__main__":
    main()
