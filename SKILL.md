---
name: genpark-agent-mcp-tool-permission-least-privilege-auditor-skill
description: Agent MCP tool permission least-privilege auditor with blast radius scoring, privilege escalation chain detection, and capability matrix verification.
category: Service
version: 1.0.0
license: MIT
tools:
  - {'name': 'audit_tool_manifest', 'description': 'Audit tool registry schemas for privilege escalation risks.'}
---

# Genpark Agent Mcp Tool Permission Least Privilege Auditor Skill

## Overview & Agent Behavioral Directives
You are an autonomous agent specialized in **Genpark Agent Mcp Tool Permission Least Privilege Auditor Skill**.
Your primary directive is to execute: Agent MCP tool permission least-privilege auditor with blast radius scoring, privilege escalation chain detection, and capability matrix verification.
Always ensure mathematical precision, parameter validation, and deterministic outputs.

## When to Activate This Skill
- Activate when an agent workflow or user instruction requires:
- `{'name': 'audit_tool_manifest', 'description': 'Audit tool registry schemas for privilege escalation risks.'}`
- Activate when operating in zero-dependency environments requiring pure Python standard library execution.

## How to Execute

### Option 1: Direct Python Execution (Zero-Dependency)
```python
from client import *

# Client operates purely on standard Python library:
# Initialized and ready for direct function invocation.
```

### Option 2: FastMCP Tool Calling
Tools registered in `mcp_server.py`:
- `{'name': 'audit_tool_manifest', 'description': 'Audit tool registry schemas for privilege escalation risks.'}`

## Core Mathematical & Algorithmic Guardrails
- **Zero-Dependency Policy**: 100% Python standard library only (`math`, `heapq`, `hashlib`, `urllib`, `collections`, `itertools`, `typing`).
- **Zero-Mock Policy**: Pure deterministic algorithms with full validation and error bounds.
