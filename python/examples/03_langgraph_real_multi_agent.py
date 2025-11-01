"""
03: Real LangGraph Multi-Agent Workflow with Visualization
===========================================================

This example demonstrates a REAL multi-agent system using actual LangGraph:
- Build a true LangGraph workflow with StateGraph
- Visualize the graph using LangGraph's built-in tools
- Multiple specialized agents collaborating
- Real agent pattern implementation

Based on:
- LangChain docs: https://docs.langchain.com/oss/python/langchain/overview
- LangGraph multi-agent: https://blog.langchain.com/langgraph-multi-agent-workflows
"""

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage
from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolNode
from langchain_core.tools import tool
from typing import Annotated, Sequence, TypedDict, Union
import operator

# Load environment variables
load_dotenv('python/.env')

# Define the state for our multi-agent workflow
class AgentState(TypedDict):
    """State shared between agents in the workflow."""
    messages: Annotated[Sequence[Union[HumanMessage, AIMessage, ToolMessage]], operator.add]
    next_agent: str  # Which agent should act next

# Define tools for our agents
@tool
def research_tool(query: str) -> str:
    """Perform research on a given query.
    
    Args:
        query: The research question or topic
        
    Returns:
        A summary of findings
    """
    # In a real implementation, this would call actual APIs
    return f"Research findings on: {query}. Key insights include [placeholder data]. " \
           "This demonstrates how tools can be used by agents in workflows."

@tool
def write_tool(topic: str, context: str) -> str:
    """Write content about a topic based on provided context.
    
    Args:
        topic: The topic to write about
        context: Supporting context or research findings
        
    Returns:
        Written content
    """
    return f"Content written about: {topic}. Incorporating context: {context[:100]}..."

@tool
def review_tool(content: str) -> str:
    """Review and provide feedback on content.
    
    Args:
        content: The content to review
        
    Returns:
        Review feedback and suggestions
    """
    return f"Review complete. Feedback: Content is well-structured and informative."

def create_research_agent() -> ChatOpenAI:
    """Create the research agent."""
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0,
        model_kwargs={"seed": 42}
    )
    return llm

def create_writer_agent() -> ChatOpenAI:
    """Create the writer agent."""
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0.7,  # More creative for writing
        model_kwargs={"seed": 42}
    )
    return llm

def create_reviewer_agent() -> ChatOpenAI:
    """Create the reviewer agent."""
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0,
        model_kwargs={"seed": 42}
    )
    return llm

def research_node(state: AgentState) -> AgentState:
    """Node: Research agent performs research."""
    print("   🔍 Research agent: Gathering information...")
    
    llm = create_research_agent()
    
    # Get the last human message
    last_message = state["messages"][-1]
    query = last_message.content if hasattr(last_message, 'content') else str(last_message)
    
    # Bind tools to the LLM
    agent_with_tools = llm.bind_tools([research_tool])
    
    # Call the agent
    response = agent_with_tools.invoke(state["messages"])
    
    return {
        "messages": [response],
        "next_agent": "writer"
    }

def writer_node(state: AgentState) -> AgentState:
    """Node: Writer agent creates content."""
    print("   ✍️  Writer agent: Creating content...")
    
    llm = create_writer_agent()
    
    # Bind tools to the LLM
    agent_with_tools = llm.bind_tools([write_tool])
    
    # Call the agent
    response = agent_with_tools.invoke(state["messages"])
    
    return {
        "messages": [response],
        "next_agent": "reviewer"
    }

def reviewer_node(state: AgentState) -> AgentState:
    """Node: Reviewer agent reviews content."""
    print("   📋 Reviewer agent: Reviewing content...")
    
    llm = create_reviewer_agent()
    
    # Bind tools to the LLM
    agent_with_tools = llm.bind_tools([review_tool])
    
    # Call the agent
    response = agent_with_tools.invoke(state["messages"])
    
    return {
        "messages": [response],
        "next_agent": END
    }

def routing_logic(state: AgentState) -> str:
    """Routing logic: Determines which agent acts next."""
    # Check the last message to see if we need to execute tools
    last_message = state["messages"][-1]
    
    # If the agent wants to call tools, execute them
    if hasattr(last_message, 'tool_calls') and last_message.tool_calls:
        return "tools"
    
    # Otherwise, go to the next agent
    next_agent = state.get("next_agent", "writer")
    if next_agent == END:
        return END
    
    return next_agent

def create_multi_agent_graph() -> StateGraph:
    """Create the multi-agent workflow graph."""
    print("🔧 Building LangGraph workflow...")
    
    # Initialize the graph
    workflow = StateGraph(AgentState)
    
    # Add nodes for each agent
    workflow.add_node("research", research_node)
    workflow.add_node("writer", writer_node)
    workflow.add_node("reviewer", reviewer_node)
    
    # Add a tools node to execute tool calls
    tools = [research_tool, write_tool, review_tool]
    workflow.add_node("tools", ToolNode(tools))
    
    # Set entry point
    workflow.set_entry_point("research")
    
    # Add conditional edges based on routing logic
    workflow.add_conditional_edges(
        "research",
        routing_logic,
        {
            "tools": "tools",
            "writer": "writer",
            END: END
        }
    )
    
    workflow.add_conditional_edges(
        "writer",
        routing_logic,
        {
            "tools": "tools",
            "reviewer": "reviewer",
            END: END
        }
    )
    
    workflow.add_conditional_edges(
        "reviewer",
        routing_logic,
        {
            "tools": "tools",
            END: END
        }
    )
    
    # After executing tools, return to the calling agent
    workflow.add_edge("tools", "reviewer")
    
    return workflow.compile()

def visualize_graph(graph: StateGraph):
    """Visualize the LangGraph workflow."""
    print("📊 Generating graph visualization...")
    
    # Use LangGraph's built-in visualization
    try:
        # Get the graph structure
        graph_mermaid = graph.get_graph().draw_mermaid()
        print(f"\n✅ Graph structure:\n{graph_mermaid}")
        
        # Save to file
        os.makedirs("python/visualizations", exist_ok=True)
        with open("python/visualizations/03_langgraph_mermaid.txt", "w") as f:
            f.write(graph_mermaid)
        print("✅ Saved Mermaid diagram to: python/visualizations/03_langgraph_mermaid.txt")
        print("\n💡 Tip: Copy the Mermaid code to https://mermaid.live/ to view the graph!")
        
    except Exception as e:
        print(f"⚠️  Could not generate Mermaid diagram: {e}")
    
    # Try to get PNG visualization if available
    try:
        graph_png = graph.get_graph().draw_mermaid_png()
        output_path = "python/visualizations/03_langgraph_workflow.png"
        os.makedirs("python/visualizations", exist_ok=True)
        with open(output_path, "wb") as f:
            f.write(graph_png)
        print(f"✅ Saved PNG diagram to: {output_path}")
    except Exception as e:
        print(f"⚠️  Could not generate PNG diagram: {e}")
        print("   This is okay - you can still view the Mermaid diagram online!")

def main():
    """Run the real LangGraph multi-agent demonstration."""
    print("🚀 Real LangGraph Multi-Agent Workflow\n")
    print("=" * 60)
    
    # Create the graph
    graph = create_multi_agent_graph()
    
    # Visualize the graph
    visualize_graph(graph)
    
    # Run the workflow
    print("\n" + "=" * 60)
    print("🤖 Running multi-agent workflow...")
    print("=" * 60)
    
    initial_state = {
        "messages": [HumanMessage(content="Research and create a summary about multi-agent AI systems.")],
        "next_agent": "writer"
    }
    
    print("\n📝 Task: Research and create a summary about multi-agent AI systems")
    print("\n🔄 Agent collaboration starting...\n")
    
    # Execute the workflow
    final_state = graph.invoke(initial_state)
    
    print("\n" + "=" * 60)
    print("✅ Workflow complete!")
    print("=" * 60)
    
    # Show the final messages
    print("\n📨 Final agent messages:")
    for i, msg in enumerate(final_state["messages"]):
        if isinstance(msg, HumanMessage):
            print(f"\n👤 Human: {msg.content}")
        elif isinstance(msg, AIMessage):
            if hasattr(msg, 'tool_calls') and msg.tool_calls:
                print(f"\n🤖 Agent: Calling tools: {[tc['name'] for tc in msg.tool_calls]}")
            else:
                print(f"\n🤖 Agent: {msg.content[:200]}...")
        elif isinstance(msg, ToolMessage):
            print(f"\n🔧 Tool Result: {msg.content[:150]}...")
    
    print("\n" + "=" * 60)
    print("🎓 Learning Summary")
    print("=" * 60)
    print("\n✅ You've learned:")
    print("   • How to create a REAL LangGraph multi-agent workflow")
    print("   • Building StateGraph with multiple nodes")
    print("   • Implementing routing logic between agents")
    print("   • Using ToolNode for tool execution")
    print("   • Visualizing workflows with Mermaid diagrams")
    print("\n💡 Next steps:")
    print("   1. Modify the agents' prompts and tools")
    print("   2. Add more agents to the workflow")
    print("   3. Experiment with different routing logic")
    print("   4. Try the interactive notebook: jupyter lab python/notebooks/")
    print("\n📚 Resources:")
    print("   • LangChain Docs: https://docs.langchain.com/oss/python/langchain/overview")
    print("   • LangGraph: https://langchain-ai.github.io/langgraph/")
    print("   • Multi-Agent Guide: https://blog.langchain.com/langgraph-multi-agent-workflows")

if __name__ == "__main__":
    main()

