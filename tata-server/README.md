# Tata MCP Server

A simple Model Context Protocol (MCP) server built with FastMCP in Python.

## Features

- **Tool**: `tata` - Returns "terve Maailma"
- **Transport**: SSE (Server-Sent Events) on HTTP port 8000
- **Framework**: FastMCP
- **Protocol**: MCP (Model Context Protocol)

## Setup

### Using uv (recommended)

```bash
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
uv pip install -e .
```

### Using pip

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -e .
```

## Running the Server

Start the server:

```bash
python server.py
```

The server will start on `http://0.0.0.0:8000` with SSE transport.

## Testing the Tool

The server supports SSE (Server-Sent Events) transport over HTTP.

### Test with HTTP

Check if server is running:
```bash
curl http://localhost:8000/health
```

### Test with MCP Client

Configure your MCP client to connect to this server:

```json
{
  "mcpServers": {
    "tata-server": {
      "command": "python",
      "args": ["server.py"],
      "cwd": "/Users/matti.venta/TestMcp/tata-server"
    }
  }
}
```

Or for HTTP/SSE transport:
```json
{
  "mcpServers": {
    "tata-server": {
      "url": "http://localhost:8000/sse"
    }
  }
}
```

## Tool Details

### `tata`

**Description**: Returns "terve Maailma" greeting.

**Parameters**: None

**Returns**: "terve Maailma"

## Architecture

- Built with FastMCP framework following CodeContext-MCP patterns
- Uses approved dependencies from organizational catalog
- Implements proper error handling and type hints
- Simple, focused implementation without over-engineering
