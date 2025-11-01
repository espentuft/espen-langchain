"""
Setup and Overview - Start Here
=================================

This Python script is your entry point. Run it to:
1. Verify your environment
2. Import necessary libraries
3. Run quick tests

To convert to Jupyter notebook, run:
  jupyter nbconvert --to notebook setup_and_overview.py
"""

import os
import sys

# Check Python version
print(f"Python: {sys.version}\n")

# Verify installations
print("Verifying installations...")
try:
    import langchain
    import langgraph
    print(f"✅ LangChain: {langchain.__version__}")
    print(f"✅ LangGraph installed")
except ImportError as e:
    print(f"❌ Missing: {e}")
    sys.exit(1)

# Configure API keys
from dotenv import load_dotenv
load_dotenv('python/.env')

api_key = os.getenv('OPENAI_API_KEY')
if api_key and api_key != 'your_openai_api_key_here':
    print("✅ OpenAI API key configured")
else:
    print("⚠️ Please set OPENAI_API_KEY in python/.env")
    
langsmith_key = os.getenv('LANGCHAIN_API_KEY')
if langsmith_key and langsmith_key != 'your_langsmith_api_key_here':
    print("✅ LangSmith API key configured (observability enabled)")
else:
    print("ℹ️ LangSmith not configured (optional for debugging)")

print("\n" + "=" * 60)
print("Ready to learn! Next steps:")
print("1. Run: python python/examples/01_simple_agent.py")
print("2. Run: python python/examples/02_multi_agent_graph.py")
print("3. Start Jupyter: jupyter notebook python/notebooks/")
print("=" * 60)

