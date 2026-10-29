# genpark-agent-mcp-tool-permission-least-privilege-auditor-skill

[![Organization](https://img.shields.io/badge/AlphaPark-OpenSource-blue.svg)](https://github.com/alphaparkinc)
[![Model Context Protocol](https://img.shields.io/badge/MCP-Standard-orange.svg)](https://modelcontextprotocol.io)
[![Zero-Dependency](https://img.shields.io/badge/Dependencies-Zero_External-brightgreen.svg)](#)
[![Python Version](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](#)
[![Security Rating](https://img.shields.io/badge/Security-Production_Hardened-success.svg)](#)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Production-hardened Agentic Cybersecurity & Red-Teaming skill engineered strictly with Python standard library. Provides real-time injection fuzzing, exfiltration canary detection, least-privilege tool sandboxing, and cryptographic audit proofs via the Model Context Protocol (MCP).

---

## Architecture & Data Flow

```mermaid
flowchart TD
    Payload[Untrusted Prompt / RAG Context / Agent Action] --> Inspector[Telemetry Ingestion]
    Inspector --> Core["GenParkAgentMCPToolPermissionLeastPrivilegeAuditor"]
    Core --> Detection[Cryptographic / Heuristic Analysis Engine]
    Detection --> Mitigation[Least-Privilege & Boundary Enforcement]
    Mitigation --> MCPOutput[MCP Result / Quarantine Signal / Merkle Seal]
```

---

## Quickstart & Usage

### 1. Direct Python Client Execution
```bash
python example_usage.py
```

### 2. Standalone MCP Server Launch
Run the native STDIO MCP server:
```bash
python mcp_server.py
```

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
