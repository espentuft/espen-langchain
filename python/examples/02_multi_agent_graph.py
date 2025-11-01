"""
02: Multi-Agent Workflow with LangGraph Visualization
======================================================

This example demonstrates a multi-agent system where agents collaborate:
- Visual learning through graph structures
- Multiple specialized agents working together
- Graph-based workflows with LangGraph

Based on LangGraph patterns: https://blog.langchain.com/langgraph-multi-agent-workflows
"""

import os
import matplotlib.pyplot as plt
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage
from langchain_anthropic import ChatAnthropic
from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolNode
import networkx as nx
from typing import Annotated, Literal
import operator

# Load environment variables
load_dotenv('python/.env')

def plot_agent_graph():
    """
    Visualize the multi-agent workflow as a graph.
    This is where the visual learning happens!
    """
    # Create a directed graph
    G = nx.DiGraph()
    
    # Define agents as nodes
    agents = {
        'Supervisor': {'color': '#FF6B6B', 'type': 'Orchestrator'},
        'Researcher': {'color': '#4ECDC4', 'type': 'Specialist'},
        'Writer': {'color': '#95E1D3', 'type': 'Specialist'},
        'Quality': {'color': '#F38181', 'type': 'Specialist'},
    }
    
    # Add nodes
    for agent, attrs in agents.items():
        G.add_node(agent, **attrs)
    
    # Define workflow edges
    # Supervisor coordinates all agents
    G.add_edge('Supervisor', 'Researcher', label='Research Task')
    G.add_edge('Supervisor', 'Writer', label='Write Content')
    G.add_edge('Researcher', 'Writer', label='Findings')
    G.add_edge('Writer', 'Quality', label='Draft Review')
    G.add_edge('Quality', 'Supervisor', label='Final Check')
    
    # Create visualization
    fig, ax = plt.subplots(figsize=(14, 10))
    fig.suptitle('Multi-Agent Workflow Architecture', fontsize=16, fontweight='bold')
    
    # Use a circular layout for better visualization
    pos = nx.spring_layout(G, k=3, iterations=50, seed=42)
    
    # Draw nodes with colors
    node_colors = [agents[node]['color'] for node in G.nodes()]
    nx.draw_networkx_nodes(G, pos, node_color=node_colors, 
                          node_size=3000, alpha=0.9, 
                          ax=ax, edgecolors='white', linewidths=2)
    
    # Draw edges
    nx.draw_networkx_edges(G, pos, edge_color='#34495e', 
                          width=2.5, alpha=0.6, arrows=True, 
                          arrowsize=20, arrowstyle='->', 
                          connectionstyle='arc3,rad=0.1', ax=ax)
    
    # Add labels
    labels = {node: node for node in G.nodes()}
    nx.draw_networkx_labels(G, pos, labels, font_size=10, 
                           font_weight='bold', font_color='white', ax=ax)
    
    # Add edge labels
    edge_labels = nx.get_edge_attributes(G, 'label')
    nx.draw_networkx_edge_labels(G, pos, edge_labels, font_size=8, 
                                bbox=dict(boxstyle='round,pad=0.3', 
                                         facecolor='white', alpha=0.8), ax=ax)
    
    # Add legend
    legend_elements = [
        plt.Line2D([0], [0], marker='o', color='w', 
                   markerfacecolor='#FF6B6B', markersize=10, label='Orchestrator'),
        plt.Line2D([0], [0], marker='o', color='w', 
                   markerfacecolor='#4ECDC4', markersize=10, label='Specialist'),
    ]
    ax.legend(handles=legend_elements, loc='upper right', fontsize=10)
    
    ax.set_facecolor('#f8f9fa')
    ax.axis('off')
    plt.tight_layout()
    
    # Save the visualization
    output_path = 'python/visualizations/02_multi_agent_graph.png'
    plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
    print(f"\n✅ Graph visualization saved to: {output_path}")
    
    return G

class MockAgent:
    """Mock agent for demonstration purposes."""
    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    
    def process(self, task):
        """Process a task and return result."""
        response = self.llm.invoke([HumanMessage(content=f"Role: {self.role}\nTask: {task}")])
        return response.content

def simulate_multi_agent_workflow():
    """
    Simulate a multi-agent workflow where agents collaborate.
    This demonstrates the 'Tool Calling' pattern from LangChain docs.
    """
    print("\n" + "=" * 60)
    print("🤖 Multi-Agent Workflow Simulation")
    print("=" * 60)
    
    # Create agents
    supervisor = MockAgent("Supervisor", "Coordinate research and writing")
    researcher = MockAgent("Researcher", "Find relevant information")
    writer = MockAgent("Writer", "Create written content")
    
    # Simulate workflow
    print("\n1️⃣ Supervisor receives task: 'Research AI trends'")
    supervisor_response = supervisor.process("Coordinate: Research AI trends and write summary")
    print(f"   👉 Supervisor: {supervisor_response[:100]}...")
    
    print("\n2️⃣ Researcher performs search")
    research_results = researcher.process("Find latest AI trends in 2025")
    print(f"   👉 Researcher: {research_results[:100]}...")
    
    print("\n3️⃣ Writer creates summary")
    summary = writer.process(f"Write a summary based on: {research_results[:200]}")
    print(f"   👉 Writer: {summary[:100]}...")
    
    print("\n4️⃣ Quality check (simulated)")
    quality_check = supervisor.process(f"Review this summary: {summary[:200]}")
    print(f"   👉 Supervisor: Quality check complete")
    
    print("\n✅ Multi-agent workflow complete!")
    print("=" * 60)

def main():
    """Run the multi-agent demonstration."""
    print("🚀 Multi-Agent Workflow with Visual Learning\n")
    
    # Step 1: Create and visualize the graph
    print("📊 Step 1: Creating workflow visualization...")
    graph = plot_agent_graph()
    print(f"   Nodes: {graph.number_of_nodes()}")
    print(f"   Edges: {graph.number_of_edges()}")
    
    # Step 2: Simulate the workflow
    print("\n🤖 Step 2: Simulating multi-agent collaboration...")
    simulate_multi_agent_workflow()
    
    print("\n" + "=" * 60)
    print("🎓 Learning Summary")
    print("=" * 60)
    print("\n✅ You've learned:")
    print("   • Multi-agent architecture patterns")
    print("   • Graph-based workflow visualization")
    print("   • Agent collaboration and task delegation")
    print("   • Tool Calling vs Handoff patterns")
    print("\n💡 Next: Check out notebooks/ for interactive Jupyter examples")
    print("📚 Docs: https://docs.langchain.com/oss/python/langchain/multi-agent")

if __name__ == "__main__":
    main()

