#!/bin/bash

# Run the Python MCP server with uv (script mode, no package build)
cd "$(dirname "$0")" && uv run python server.py
