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


@mcp.tool()
def universal(value: str) -> str:
    """
    Universal tool that repeats a given value 10 times with '****' between each occurrence

    Args:
        value: The specific value to repeat

    Returns:
        The value repeated 10 times with '****' as separator
    """
    return "****".join([value] * 10)


if __name__ == "__main__":
    # Run the server with HTTP transport on port 8000
    mcp.run(transport="http", host="0.0.0.0", port=8000)
