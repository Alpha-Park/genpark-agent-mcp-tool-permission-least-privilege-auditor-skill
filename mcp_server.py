# -*- coding: utf-8 -*-
import sys, json
from client import GenParkAgentMCPToolPermissionLeastPrivilegeAuditor

auditor = GenParkAgentMCPToolPermissionLeastPrivilegeAuditor()

def run_tool(name, args):
    if name == "audit_tool_manifest":
        tools = args.get("tools", [])
        return auditor.audit_tool_manifest(tools)
    else:
        raise ValueError(f"Unknown tool: {name}")

from typing import Any, Dict, List, Optional

try:
    from mcp.server.fastmcp import FastMCP
except ImportError as exc:
    raise SystemExit("MCP requires the mcp package. Run: python -m pip install -r requirements.txt") from exc

mcp = FastMCP('genpark-agent-mcp-tool-permission-least-privilege-auditor-skill')

@mcp.tool()
def audit_tool_manifest(tools: Optional[List[Dict[str, Any]]] = None) -> str:
    """Audit a supplied tool manifest for excessive privileges."""
    return json.dumps(run_tool('audit_tool_manifest', {'tools': tools if tools is not None else []}))

def main():
    if "--test" in sys.argv:
        print("[TEST] Running GenPark MCP Least-Privilege Auditor Self-Test...")
        test_tools = [
            {"name": "fetch_url", "capabilities": ["network_get"]},
            {"name": "execute_bash", "capabilities": ["exec"], "parameters": {"properties": {"command": {}}}}
        ]
        res = auditor.audit_tool_manifest(test_tools)
        assert res["least_privilege_compliant"] is False, "Should flag RCE escalation chain"
        assert len(res["escalation_vectors"]) > 0
        print("[TEST] All tests passed successfully!")
        return

    mcp.run(transport="stdio")

if __name__ == "__main__":
    main()
