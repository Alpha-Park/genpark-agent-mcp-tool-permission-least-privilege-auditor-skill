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

    for line in sys.stdin:
        if not line.strip(): continue
        try:
            req = json.loads(line)
            res = run_tool(req.get("name"), req.get("arguments", {}))
            print(json.dumps({"jsonrpc": "2.0", "id": req.get("id"), "result": res}))
        except Exception as e:
            print(json.dumps({"jsonrpc": "2.0", "id": None, "error": {"code": -32603, "message": str(e)}}))
        sys.stdout.flush()

if __name__ == "__main__":
    main()
