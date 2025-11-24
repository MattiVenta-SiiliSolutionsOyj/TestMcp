#!/bin/bash

# Pre-deploy script for tata-mcp-server
# Runs validation checks before deployment

set -e  # Exit on any error

echo "🚀 Starting pre-deploy checks..."

# Navigate to tata-server directory
cd "$(dirname "$0")/tata-server"

echo "📦 Syncing dependencies..."
uv sync

echo "✅ Dependencies synced successfully"

echo "🔍 Running Python syntax check..."
uv run python -m py_compile server.py

echo "✅ Python syntax check passed"

echo "🧪 Testing server import..."
uv run python -c "from fastmcp import FastMCP; print('FastMCP import successful')"

echo "✅ All pre-deploy checks passed!"
echo "🎉 Ready to deploy"
