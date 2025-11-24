"""
Tata MCP Server - A simple MCP server using FastMCP
Returns 'terve Maailma' when tata tool is called
"""

from fastmcp import FastMCP

# Create FastMCP server instance
mcp = FastMCP("tata-mcp-server")


@mcp.tool()
def tata() -> str:
    """Returns 'terve Maailma' greeting"""
    return "terve Maailma"


if __name__ == "__main__":
    # Run the server with HTTP transport on port 8000
    mcp.run(transport="http", host="0.0.0.0", port=8000)
