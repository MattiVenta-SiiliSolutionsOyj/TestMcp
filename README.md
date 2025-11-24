# Test MCP Server

A simple Model Context Protocol (MCP) server with HTTP transport for testing purposes.

## Features

- **Tool**: `terve_maailma` - Returns "Terve maailma!" (Hello world in Finnish)
- **Transport**: HTTP on port 8000
- **Protocol**: MCP (Model Context Protocol)

## Setup

Install dependencies:

```bash
npm install
```

## Running the Server

Start the server:

```bash
npm start
```

The server will start on `http://localhost:8000`.

## Testing the Tool

The server supports both:
1. **HTTP transport** on port 8000 (POST to `/mcp`)
2. **stdio transport** for local MCP clients

### Test with HTTP

Check if server is running:
```bash
curl http://localhost:8000
```

### Test with MCP Client

Configure your MCP client to connect to this server using stdio transport:

```json
{
  "mcpServers": {
    "test-server": {
      "command": "node",
      "args": ["server.js"],
      "cwd": "/path/to/TestMcp"
    }
  }
}
```

## Tool Details

### `terve_maailma`

**Description**: A simple test tool that returns a Finnish greeting.

**Parameters**:
- `name` (optional string): Name to greet

**Examples**:
- Without parameter: Returns "Terve maailma!"
- With name: Returns "Terve, [name]!"
