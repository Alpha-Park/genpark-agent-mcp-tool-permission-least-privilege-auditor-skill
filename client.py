# -*- coding: utf-8 -*-
"""
GenPark Agent MCP Tool Permission Least-Privilege Auditor
Standard Library only: json, typing.
Formal capability matrix analyzer for Model Context Protocol (MCP) servers.
Evaluates blast radius, detects privilege escalation paths, and enforces sandbox boundaries.
"""

from typing import Dict, List, Any

class GenParkAgentMCPToolPermissionLeastPrivilegeAuditor:
    CAPABILITY_WEIGHTS = {
        "exec": 1.0,        # Shell / python / binary execution
        "fs_write": 0.85,    # File modification / deletion
        "network_post": 0.8, # External API posting / data export
        "db_write": 0.75,    # Database update / drop
        "fs_read": 0.4,     # File reading
        "network_get": 0.35, # Web scraping / API fetching
        "db_read": 0.3,     # Database querying
        "pure_calc": 0.05   # Math / string parsing
    }

    def __init__(self, max_allowed_blast_radius: float = 2.5):
        self.max_allowed_blast_radius = max_allowed_blast_radius

    def audit_tool_manifest(self, tools: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Audits a list of tool definitions for privilege escalation and excessive permissions.
        """
        audited_tools = []
        total_blast_radius = 0.0
        escalation_risks = []

        capabilities_present = set()

        for tool in tools:
            name = tool.get("name", "unknown")
            declared_caps = tool.get("capabilities", ["pure_calc"])
            for cap in declared_caps:
                capabilities_present.add(cap)

            tool_score = sum(self.CAPABILITY_WEIGHTS.get(c, 0.5) for c in declared_caps)

            # High risk parameters check
            params = tool.get("parameters", {}).get("properties", {})
            has_raw_command = any("command" in p.lower() or "cmd" in p.lower() for p in params)
            has_filepath = any("path" in p.lower() or "file" in p.lower() for p in params)

            if has_raw_command: tool_score *= 1.4
            if has_filepath and "fs_write" in declared_caps: tool_score *= 1.2

            total_blast_radius += tool_score

            audited_tools.append({
                "name": name,
                "tool_blast_radius": round(tool_score, 3),
                "capabilities": declared_caps,
                "has_raw_command_param": has_raw_command,
                "risk_tier": "HIGH" if tool_score >= 1.2 else ("MEDIUM" if tool_score >= 0.6 else "LOW")
            })

        # Escalation path detection:
        # e.g., network_get (untrusted input) + fs_write + exec
        if "network_get" in capabilities_present and "exec" in capabilities_present:
            escalation_risks.append({
                "vector": "REMOTE_CODE_EXECUTION_CHAIN",
                "detail": "Agent has both untrusted web fetch and shell execution capabilities."
            })
        if "fs_write" in capabilities_present and "exec" in capabilities_present:
            escalation_risks.append({
                "vector": "SCRIPT_DROP_AND_EXECUTE",
                "detail": "Agent can write arbitrary files to disk and execute commands."
            })

        is_compliant = (total_blast_radius <= self.max_allowed_blast_radius) and (len(escalation_risks) == 0)

        return {
            "total_tools": len(tools),
            "aggregate_blast_radius": round(total_blast_radius, 3),
            "max_allowed_blast_radius": self.max_allowed_blast_radius,
            "least_privilege_compliant": is_compliant,
            "escalation_vectors": escalation_risks,
            "tool_evaluations": audited_tools,
            "remediation": "Split broad execution tools into granular, read-only and pre-approved actions." if not is_compliant else "Policy compliant."
        }
