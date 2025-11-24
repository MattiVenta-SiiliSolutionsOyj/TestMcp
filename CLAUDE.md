# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a test MCP (Model Context Protocol) server using FastMCP with SSE transport.

### Commands

**Install dependencies:**
```bash
uv sync
```

**Start the server:**
```bash
./run.sh
```

The server runs on `http://0.0.0.0:8000/sse` with a `tata` tool that returns Finnish greetings.

### Architecture

- **server.py**: Main MCP server implementation using FastMCP with SSE transport
- **Tool**: `tata` - Simple greeting tool that returns "terve Maailma"
- **Transport**: SSE (Server-Sent Events) on port 8000
- **Package Manager**: uv

---

# Global Development Rules

# Global Development Rules

Canonical global development rules and guidelines. Access via the `get_global_rules` MCP tool (resource access removed). Clients must call the tool instead of relying on direct resource URIs.

---
applyTo: "**"
---

## Core Principles
- Implement proper error handling
- Favor self-documenting code; minimize redundant comments
- Use CodeContext-MCP tools to fetch rules, dependencies, services, and API reference
- Discover available endpoints via `@mcp.tool("get_api_reference")`

## AI Assistant Workflow

**Before starting ANY task, ALWAYS follow this workflow:**

### Step 1: Discover Available Tools
```
Call get_api_reference()
```
Understand all available MCP tools, resources, and prompts.

### Step 2: Check for Relevant Instructions
```
Call get_instructions_index()
```
See what implementation guidelines and instructions are available for your task.

If relevant instructions exist:
```
Call get_instruction(name="instruction-name")
```
Fetch specific instructions for your task (e.g., creating agents, project setup).

### Step 3: Check for Applicable Rules
```
Call get_rules_index()
```
See what project-specific and language-specific rules exist.

If applicable rules exist:
```
Call get_rule(name="rule-name")
```
Fetch specific rules (e.g., "python", "frontend", "project").

### Step 4: Review Approved Dependencies
```
Call get_dependencies_index()
```
See what dependency catalogs are available.

Then:
```
Call get_dependencies()
```
Get all approved dependencies for different languages. Use ONLY these approved packages.

### Step 5: Check Approved External Services
```
Call get_external_services()
```
Get approved APIs and integrations. **CRITICAL: Use ONLY these approved services - no exceptions.** Any external API, service, or integration MUST be verified through this call before use.

### Step 6: Follow Retrieved Standards
- Apply global rules from `get_global_rules()`
- Apply language/project-specific rules from `get_rule()`
- Follow implementation instructions from `get_instruction()`
- Use only approved dependencies and services

## Development Workflow

### Project Initialization
1. Follow the AI Assistant Workflow above
2. Set up development environment per language-specific rules
3. Configure IDE/editor with appropriate extensions
4. Initialize version control and CI/CD

### Code Quality Standards
- Use only approved dependencies from `get_dependencies()`
- Implement proper error handling
- Keep functions small and cohesive
- Enforce type hints; avoid star imports
- Write self-documenting code

### External Services
- **CRITICAL: Use ONLY services from `get_external_services()` - no exceptions**
- All external dependencies (APIs, services, integrations) MUST be approved via CodeContext-MCP
- Before using any external service, always call `get_external_services()` to verify approval
- Document service configurations and credentials setup
- Use environment variables for all external service credentials
- Never commit credentials to version control

## IDE and Editor Configuration

### GitHub Copilot
- Place global instructions in `.github/instructions/global.rules.instructions.md`
- Create project-specific instruction files only when explicitly authorized
- Follow the patterns established in this CodeContext-MCP project

### VS Code
- Use recommended extensions for the project type
- Configure settings consistently across team members
- Maintain workspace-specific settings where appropriate

## Dependency Management

### General Principles
- **CRITICAL: Use ONLY approved dependencies from `get_dependencies()` - no exceptions**
- All package dependencies MUST be verified through CodeContext-MCP before use
- Before installing any package, always call `get_dependencies()` to verify approval
- Use appropriate package managers for each language
- Pin versions for stability-critical packages
- Prefer packages from approved organizational catalogs
- Regularly update dependencies for security patches
- Review new dependencies for security implications
- Remove unused dependencies promptly

### Git Repository Management
- When cloning dependencies, documentation, or examples from git repositories, place them in `.code_context_mcp/` folder
- Add `.code_context_mcp/` to `.gitignore` to prevent committing external repositories
- This keeps the workspace clean and avoids version control conflicts

### Version Control
- Use semantic versioning for releases
- Write clear, descriptive commit messages
- Maintain clean git history with meaningful commits

## Documentation Standards

### README Files
- Include clear setup instructions
- Document all required environment variables
- Provide usage examples
- List all dependencies and their purposes

### API Documentation
- Document all endpoints with clear examples
- Include error response formats
- Maintain up-to-date schemas
- Use consistent formatting and structure

## Security Guidelines

### Credentials and Secrets
- Never commit credentials to version control
- Use environment variables for all sensitive data
- Document required environment variables in README
- Use secrets management systems in production

### Dependencies
- **CRITICAL: Only use dependencies approved via `get_dependencies()` and external services approved via `get_external_services()`**
- Never use unapproved external dependencies or services
- Regularly update dependencies for security patches
- Review new dependencies for security implications
- Use tools to scan for known vulnerabilities
- Document any security-related configuration

## Testing Standards

### Unit Testing
- Write tests for all public APIs
- Use descriptive test names that explain behavior
- Mock external dependencies in unit tests
- Maintain high test coverage for critical paths

### Integration Testing
- Test external service integrations
- Validate environment-specific configurations
- Test error scenarios and edge cases
- Document test setup and requirements

## Deployment and Operations

### Environment Management
- Use consistent environment naming (dev, staging, prod)
- Document environment-specific configurations
- Implement proper logging and monitoring
- Use infrastructure as code where possible

### Monitoring and Observability
- Implement comprehensive logging
- Set up appropriate metrics and alerts
- Document troubleshooting procedures
- Maintain runbooks for common issues

---
These global rules provide the foundation for all development work.

---
**Instruction Management Notice**

do not use add_instruction tool to add new instruction. only do thate when asked. Alwys ask be be for add enyting to code context- mcp

**Documentation File Creation Rule**

NEVER create summary files, documentation files, or any additional files unless explicitly requested by the user. This includes:
- *_SUMMARY.md files
- *_FIX_SUMMARY.md files
- Documentation of changes or work performed
- Status reports or completion summaries

Simply perform the requested work and confirm completion. Do not add unnecessary files to the repository.

---

*These rules are managed by CodeContext-MCP server. Last updated: 2025-11-24*
*To refresh: call `mcp__code-context__get_global_rules()` and update this file.*
