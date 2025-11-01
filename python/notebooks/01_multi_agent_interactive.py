"""
01: Interactive Multi-Agent Workflow Notebook
==============================================

This notebook (convert to .ipynb) provides an interactive learning experience for
multi-agent workflows with LangGraph. It combines:

- Visual graph exploration
- Live agent execution
- Hands-on experimentation
- Real-time debugging

To use: Convert this .py file to a Jupyter notebook
"""

import os
import sys
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from dotenv import load_dotenv

# Load environment
load_dotenv('python/.env')

# Configuration
OUTPUT_DIR = 'python/visualizations'
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ============================================================================
# CELL 1: Setup and Verification
# ============================================================================
"""
# 🚀 Setup and Verification

Let's start by verifying your environment is ready.
"""

print("🔍 Checking environment...")
print("=" * 60)

# Check Python version
print(f"✅ Python: {sys.version.split()[0]}")

# Check imports
try:
    from langchain_openai import ChatOpenAI
    from langgraph.graph import StateGraph, END
    import langchain
    import langgraph
    print(f"✅ LangChain: {langchain.__version__}")
    print(f"✅ LangGraph: {langgraph.__version__}")
except ImportError as e:
    print(f"❌ Import error: {e}")
    print("   Run: pip install langchain langgraph")

# Check API key
api_key = os.getenv('OPENAI_API_KEY')
if api_key and api_key != 'your_openai_api_key_here':
    print("✅ OpenAI API key configured")
else:
    print("⚠️  Please set OPENAI_API_KEY in python/.env")

print("=" * 60)

# ============================================================================
# CELL 2: Understanding Multi-Agent Patterns
# ============================================================================
"""
# 🎯 Understanding Multi-Agent Patterns

Let's visualize the two main patterns for multi-agent systems:
1. **Tool Calling**: Supervisor calls specialized agents as tools
2. **Handoffs**: Agents pass control directly to each other
"""

def visualize_agent_patterns():
    """Visualize the two main multi-agent patterns."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))
    
    # Pattern 1: Tool Calling
    ax1.set_title('Pattern 1: Tool Calling (Orchestration)', 
                 fontsize=14, fontweight='bold', pad=20)
    
    # Draw supervisor
    supervisor = mpatches.FancyBboxPatch((2, 2), 1.5, 1, 
                                        boxstyle="round,pad=0.1", 
                                        facecolor='#FF6B6B', 
                                        edgecolor='white', linewidth=2)
    ax1.add_patch(supervisor)
    ax1.text(2.75, 2.5, 'Supervisor', ha='center', va='center', 
            fontweight='bold', fontsize=11, color='white')
    
    # Draw specialized agents as tools
    agents = [
        ('Researcher', 0, 0, '#4ECDC4'),
        ('Writer', 3.5, 0, '#95E1D3'),
        ('Reviewer', 1, 0, '#F38181'),
    ]
    
    for name, x, y, color in agents:
        agent_box = mpatches.FancyBboxPatch((x, y), 1.2, 0.8, 
                                           boxstyle="round,pad=0.1", 
                                           facecolor=color, 
                                           edgecolor='white', linewidth=2)
        ax1.add_patch(agent_box)
        ax1.text(x + 0.6, y + 0.4, name, ha='center', va='center', 
                fontweight='bold', fontsize=10, color='white')
        
        # Draw arrows from supervisor
        ax1.arrow(2.75, 2, x + 0.6 - 2.75, y + 0.8 - 2, 
                 head_width=0.15, head_length=0.15, 
                 fc='#34495e', ec='#34495e', lw=1.5)
    
    ax1.set_xlim(-0.5, 5)
    ax1.set_ylim(-0.5, 4)
    ax1.axis('off')
    ax1.set_facecolor('#f8f9fa')
    
    # Pattern 2: Handoffs
    ax2.set_title('Pattern 2: Handoffs (Passing Control)', 
                 fontsize=14, fontweight='bold', pad=20)
    
    # Draw sequential agents
    handoff_agents = [
        ('Researcher', 0, 2, '#4ECDC4'),
        ('Writer', 2, 2, '#95E1D3'),
        ('Reviewer', 4, 2, '#F38181'),
    ]
    
    for i, (name, x, y, color) in enumerate(handoff_agents):
        agent_box = mpatches.FancyBboxPatch((x, y), 1.3, 0.8, 
                                           boxstyle="round,pad=0.1", 
                                           facecolor=color, 
                                           edgecolor='white', linewidth=2)
        ax2.add_patch(agent_box)
        ax2.text(x + 0.65, y + 0.4, name, ha='center', va='center', 
                fontweight='bold', fontsize=10, color='white')
        
        # Draw arrows between agents
        if i < len(handoff_agents) - 1:
            ax2.arrow(x + 1.3, y + 0.4, 0.5, 0, 
                     head_width=0.15, head_length=0.15, 
                     fc='#34495e', ec='#34495e', lw=1.5)
    
    ax2.set_xlim(-0.5, 6)
    ax2.set_ylim(-0.5, 4)
    ax2.axis('off')
    ax2.set_facecolor('#f8f9fa')
    
    plt.tight_layout()
    
    # Save
    output_path = f'{OUTPUT_DIR}/01_agent_patterns.png'
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"✅ Saved pattern visualization to: {output_path}")
    
    return fig

print("\n🎨 Visualizing agent patterns...")
fig = visualize_agent_patterns()
plt.show()

# ============================================================================
# CELL 3: Simple Multi-Agent Example
# ============================================================================
"""
# 🤖 Simple Multi-Agent Example

Let's build a simple multi-agent system that demonstrates the concepts.
"""

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage
from langgraph.graph import StateGraph, END
from typing import TypedDict, Annotated, Sequence
import operator

# Define state
class SimpleState(TypedDict):
    messages: Annotated[Sequence[HumanMessage | AIMessage], operator.add]
    stage: str  # Current stage in the workflow

# Create a simple 3-agent workflow
def create_simple_workflow():
    """Create a simple workflow with 3 agents."""
    print("🔧 Building simple 3-agent workflow...")
    
    # Create different agents with different personalities
    research_agent = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    writer_agent = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)
    reviewer_agent = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    
    # Define agent nodes
    def research_node(state: SimpleState) -> SimpleState:
        print("   🔍 Research Agent: Working...")
        prompt = "You are a research assistant. Analyze and summarize the topic."
        response = research_agent.invoke([HumanMessage(content=prompt), state["messages"][-1]])
        return {"messages": [response], "stage": "writer"}
    
    def writer_node(state: SimpleState) -> SimpleState:
        print("   ✍️  Writer Agent: Working...")
        prompt = "You are a content writer. Write engaging content based on the research."
        response = writer_agent.invoke([HumanMessage(content=prompt), state["messages"][-1]])
        return {"messages": [response], "stage": "reviewer"}
    
    def reviewer_node(state: SimpleState) -> SimpleState:
        print("   📋 Reviewer Agent: Working...")
        prompt = "You are a quality reviewer. Provide feedback on the content."
        response = reviewer_agent.invoke([HumanMessage(content=prompt), state["messages"][-1]])
        return {"messages": [response], "stage": END}
    
    # Build the graph
    workflow = StateGraph(SimpleState)
    workflow.add_node("research", research_node)
    workflow.add_node("writer", writer_node)
    workflow.add_node("reviewer", reviewer_node)
    
    # Define flow
    workflow.set_entry_point("research")
    workflow.add_edge("research", "writer")
    workflow.add_edge("writer", "reviewer")
    workflow.add_edge("reviewer", END)
    
    return workflow.compile()

print("\n🚀 Creating simple multi-agent workflow...")
simple_workflow = create_simple_workflow()

# Visualize it
print("\n📊 Visualizing workflow structure...")
try:
    graph_mermaid = simple_workflow.get_graph().draw_mermaid()
    print("\n" + "=" * 60)
    print("WORKFLOW GRAPH (Mermaid):")
    print("=" * 60)
    print(graph_mermaid)
    print("=" * 60)
    print("\n💡 Copy this code to https://mermaid.live/ to visualize!")
    
    # Save
    with open(f'{OUTPUT_DIR}/01_simple_workflow.txt', 'w') as f:
        f.write(graph_mermaid)
    print(f"\n✅ Saved to: {OUTPUT_DIR}/01_simple_workflow.txt")
except Exception as e:
    print(f"⚠️  Could not generate diagram: {e}")

# ============================================================================
# CELL 4: Run the Simple Workflow
# ============================================================================
"""
# ▶️ Run the Simple Workflow

Now let's execute it with a sample task!
"""

print("\n" + "=" * 60)
print("🤖 Running simple multi-agent workflow...")
print("=" * 60)

# Create initial state
initial_state = {
    "messages": [HumanMessage(content="Create a brief summary about the benefits of multi-agent AI systems.")],
    "stage": "research"
}

print("\n📝 Task: Create a brief summary about multi-agent AI systems")
print("\n🔄 Starting agent collaboration...\n")

# Run the workflow
final_state = simple_workflow.invoke(initial_state)

print("\n" + "=" * 60)
print("✅ Workflow complete!")
print("=" * 60)

# Display results
print("\n📨 Agent Outputs:\n")
for i, msg in enumerate(final_state["messages"], 1):
    if isinstance(msg, HumanMessage):
        print(f"👤 Message {i}: {msg.content[:150]}...")
    elif isinstance(msg, AIMessage):
        print(f"🤖 Agent {i}: {msg.content[:200]}...")
    print()

# ============================================================================
# CELL 5: Experiment and Customize
# ============================================================================
"""
# 🎨 Experiment and Customize

Now it's your turn! Try modifying:
- The agents' prompts
- The workflow structure
- Add more agents
- Change the order of execution
"""

print("\n" + "=" * 60)
print("🎓 Learning Complete!")
print("=" * 60)
print("\n✅ You've learned:")
print("   • Multi-agent patterns (Tool Calling vs Handoffs)")
print("   • Building LangGraph workflows")
print("   • Visualizing agent architectures")
print("   • Running agent collaborations")
print("\n💡 Next steps:")
print("   • Run: python python/examples/03_langgraph_real_multi_agent.py")
print("   • Explore LangSmith for debugging")
print("   • Build your own custom agents")
print("\n📚 Resources:")
print("   • https://docs.langchain.com/oss/python/langchain/overview")
print("   • https://langchain-ai.github.io/langgraph/")

