# Tata MCP Server

A simple Model Context Protocol (MCP) server using FastMCP with SSE transport.

## Features

- **Tool**: `tata` - Returns "terve Maailma" (Hello World in Finnish)
- **Transport**: SSE (Server-Sent Events) on port 8000
- **Protocol**: MCP (Model Context Protocol)
- **Framework**: FastMCP

## Setup

Install dependencies using uv:

```bash
uv sync
```

## Running the Server

Start the server:

```bash
./run.sh
```

Or directly with uv:

```bash
uv run python server.py
```

The server will start on `http://0.0.0.0:8000/sse`.

## Pre-Deploy Checks

Run pre-deployment validation:

```bash
./pre-deploy.sh
```

This checks dependencies, Python syntax, and imports.

## Tool Details

### `tata`

**Description**: A simple test tool that returns a Finnish greeting.

**Returns**: "terve Maailma"

## Development

- **Python Version**: 3.10+
- **Dependencies**: fastmcp>=0.3.0, uvicorn[standard]>=0.24.0
- **Package Manager**: uv
