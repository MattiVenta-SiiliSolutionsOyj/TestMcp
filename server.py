"""
Tata MCP Server - A simple MCP server using FastMCP
Demonstrates various MCP tool capabilities
"""

from fastmcp import FastMCP
from typing import List, Dict
import json
import urllib.request
import urllib.error

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


@mcp.tool()
def calculate(operation: str, a: float, b: float) -> str:
    """
    Perform basic mathematical operations

    Args:
        operation: The operation to perform (add, subtract, multiply, divide)
        a: First number
        b: Second number

    Returns:
        Result of the calculation
    """
    operations = {
        "add": a + b,
        "subtract": a - b,
        "multiply": a * b,
        "divide": a / b if b != 0 else "Error: Division by zero"
    }

    result = operations.get(operation.lower(), "Error: Unknown operation")
    return f"{operation}({a}, {b}) = {result}"


@mcp.tool()
def get_info(category: str) -> str:
    """
    Get information about different categories

    Args:
        category: Category to get info about (server, tools, mcp)

    Returns:
        Information about the requested category
    """
    tool_list = [
        "tata",
        "universal",
        "calculate",
        "get_info",
        "list_items",
        "format_data",
        "get_linnanmaa_weather",
        "allatools"
    ]
    info = {
        "server": "FastMCP server running on Python with SSE transport",
        "tools": f"This server provides: {', '.join(tool_list)}",
        "mcp": "Model Context Protocol - A protocol for communication between AI models and tools",
        "allatools": ", ".join(tool_list)
    }

    return info.get(category.lower(), f"No information available for category: {category}")
@mcp.tool()
def allatools() -> str:
    """
    Returns a comma-separated list of all available tool names
    """
    return ", ".join([
        "tata",
        "universal",
        "calculate",
        "get_info",
        "list_items",
        "format_data",
        "get_linnanmaa_weather",
        "allatools"
    ])


@mcp.tool()
def list_items(items: List[str], separator: str = ", ") -> str:
    """
    Format a list of items with a custom separator

    Args:
        items: List of items to format
        separator: Separator to use between items (default: ", ")

    Returns:
        Formatted string of items
    """
    return separator.join(items)


@mcp.tool()
def format_data(data: Dict[str, str], format_type: str = "json") -> str:
    """
    Format dictionary data in different formats

    Args:
        data: Dictionary data to format
        format_type: Output format (json, text, list)

    Returns:
        Formatted data string
    """
    if format_type == "json":
        return json.dumps(data, indent=2)
    elif format_type == "text":
        return "\n".join([f"{k}: {v}" for k, v in data.items()])
    elif format_type == "list":
        return "\n".join([f"- {k} = {v}" for k, v in data.items()])
    else:
        return "Error: Unknown format type"


@mcp.tool()
def get_linnanmaa_weather() -> str:
    """
    Fetch current weather from Linnanmaa Weather Station, Oulu, Finland

    Uses the official University of Oulu campus weather station operated by
    VTT Technical Research Centre and Vaisala Oyj since 1987.

    Returns:
        Real-time weather data from Linnanmaa including temperature, humidity,
        pressure, wind speed/direction, precipitation, and more
    """
    try:
        # Using approved Linnanmaa Weather Station API
        # Location: University of Oulu (65.03°N, 25.48°E, 13m altitude)
        url = "https://weather.willab.fi/weather.json"

        with urllib.request.urlopen(url, timeout=10) as response:
            data = json.loads(response.read().decode())

        # Convert wind direction to compass direction
        wind_deg = data.get('winddir', 0)
        directions = ['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE',
                      'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW']
        wind_compass = directions[round(wind_deg / 22.5) % 16]

        result = f"""Weather at Linnanmaa Weather Station, Oulu
(University of Oulu campus - VTT/Vaisala station)

Temperature: {data.get('tempnow', 'N/A')}°C (Low: {data.get('templo', 'N/A')}°C, High: {data.get('temphi', 'N/A')}°C)
Dew Point: {data.get('dewpoint', 'N/A')}°C
Wind Chill: {data.get('windchill', 'N/A')}°C
Humidity: {data.get('humidity', 'N/A')}%
Air Pressure: {data.get('airpressure', 'N/A')} hPa
Wind Speed: {data.get('windspeed', 'N/A')} m/s (Max: {data.get('windspeedmax', 'N/A')} m/s)
Wind Direction: {wind_deg}° ({wind_compass})
Precipitation: {data.get('precipitation1h', 'N/A')} mm (1h), {data.get('precipitation1d', 'N/A')} mm (24h)
Solar Radiation: {data.get('solarrad', 'N/A')} W/m²

Coordinates: 65.03°N, 25.48°E (Altitude: 13m)
Last Updated: {data.get('timestamp', 'N/A')}"""

        return result

    except urllib.error.URLError as e:
        return f"Error fetching weather data from Linnanmaa station: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"


if __name__ == "__main__":
    # Run the server with HTTP transport on port 8000
    mcp.run(transport="http", host="0.0.0.0", port=8000)
