#!/bin/bash

echo "🚀 GPT-RPG System Installation Script"
echo "------------------------------------"

# Ensure Python is installed
if ! command -v python3 &>/dev/null; then
    echo "❌ Python3 is not installed. Please install Python3 and retry."
    exit 1
fi

# Install dependencies
echo "📦 Installing dependencies..."
pip install -r requirements.txt

# Check if installation was successful
if [ $? -eq 0 ]; then
    echo "✅ GPT-RPG System is successfully installed!"
else
    echo "❌ Installation failed. Please check the error messages above."
    exit 1
fi