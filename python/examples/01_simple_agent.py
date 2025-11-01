"""
01: Simple LangChain Agent with Visual Output
==============================================

This is your first hands-on example - a simple agent that demonstrates:
- Basic LangChain setup
- Creating an agent with tools
- Running and visualizing the workflow

Based on: https://docs.langchain.com/oss/python/langchain/overview
"""

import os
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI

# Load environment variables
load_dotenv('python/.env')

def get_weather(city: str) -> str:
    """Get weather for a given city."""
    # This is a mock function - in production, you'd call a real API
    return f"It's always sunny in {city}! ☀️"

def main():
    """Run a simple agent example."""
    print("🚀 Simple LangChain Agent Demo\n")
    print("=" * 60)
    
    # Create the agent
    # According to docs: https://docs.langchain.com/oss/python/langchain/overview
    agent = create_agent(
        model="gpt-4o-mini",  # Using a cost-effective model for learning
        tools=[get_weather],
        system_prompt="You are a helpful assistant with access to weather information.",
    )
    
    print("\n📊 Agent Created Successfully!")
    print(f"   Model: gpt-4o-mini")
    print(f"   Tools: {[t.name for t in agent.tools]}")
    
    # Run the agent
    print("\n" + "=" * 60)
    print("💬 Running conversation...\n")
    
    response = agent.invoke(
        {"messages": [{"role": "user", "content": "What is the weather in San Francisco?"}]}
    )
    
    print("=" * 60)
    print("\n✅ Response received!")
    print(f"\n{response['messages'][-1].content}")
    print("\n" + "=" * 60)
    print("\n🎉 First agent demo complete!")
    print("\n💡 Next: Check out '02_multi_agent_graph.py' to see agents working together")

if __name__ == "__main__":
    main()

