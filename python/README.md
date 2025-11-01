# LangChain & LangGraph Learning Environment

A **visual-first** learning environment for building multi-agent workflows with LangChain and LangGraph, optimized for design leaders and AI-native builders.

## 🎯 Learning Philosophy

This project emphasizes **visual learning** and **hands-on exploration**:

- **See it**: Visual graphs and workflows
- **Try it**: Interactive examples and notebooks  
- **Build it**: Start simple, then expand
- **Debug it**: LangSmith integration for observability

## 🚀 Quick Start

### 1. Set Up Environment

```bash
# Navigate to project root
cd /Users/espentuft/Documents/production/espen-langchain

# Activate Python virtual environment
source venv/bin/activate

# Configure API keys
cp python/.env.example python/.env
# Edit python/.env with your API keys
```

### 2. Run Your First Examples

```bash
# Simple agent demo
python python/examples/01_simple_agent.py

# Multi-agent workflow with visualization
python python/examples/02_multi_agent_graph.py

# Setup verification
python python/notebooks/00_setup_and_overview.py
```

### 3. Launch Jupyter for Interactive Learning

```bash
# Start Jupyter Lab
jupyter lab python/notebooks/

# Or start classic notebook
jupyter notebook python/notebooks/
```

## 📁 Project Structure

```
python/
├── examples/           # Runnable examples demonstrating concepts
│   ├── 01_simple_agent.py       # Basic agent setup
│   └── 02_multi_agent_graph.py  # Multi-agent workflows
├── agents/             # Reusable agent implementations
├── visualizations/     # Generated graphs and charts
├── notebooks/          # Interactive Jupyter notebooks
└── .env               # API keys (create from .env.example)

visualizations/
└── 02_multi_agent_graph.png  # Generated workflow diagrams
```

## 📚 Learning Path

### Beginner Path

1. ✅ **Setup Verification** (`00_setup_and_overview.py`)
   - Verify environment
   - Configure API keys
   - Test imports

2. 🤖 **Simple Agent** (`01_simple_agent.py`)
   - Create your first agent
   - Add tools
   - Run basic conversation

3. 🎨 **Multi-Agent Graph** (`02_multi_agent_graph.py`)
   - Visualize agent workflows
   - Understand collaboration patterns
   - See graph-based architecture

### Advanced Path (Coming Soon)

4. 🔧 **Custom Agents**
   - Build specialized agents
   - Tool integration
   - State management

5. 🏗️ **Complex Workflows**
   - Multi-stage pipelines
   - Conditional routing
   - Human-in-the-loop

6. 📊 **Production Patterns**
   - Error handling
   - Observability with LangSmith
   - Performance optimization

## 🛠️ Tools & Technologies

### Core

- **LangChain**: Framework for building LLM applications
- **LangGraph**: Graph-based agent orchestration
- **OpenAI**: GPT models for agents
- **Anthropic** (optional): Claude models

### Visualization

- **Matplotlib**: Graphs and charts
- **NetworkX**: Graph structures
- **Jupyter**: Interactive notebooks

### Observability

- **LangSmith**: Debug, test, and monitor agents
- **Traces**: View agent execution paths
- **Metrics**: Performance and cost tracking

## 🎓 Key Concepts

### Agent Patterns

1. **Tool Calling**: Supervisor agent calls specialized agents
   - Good for: Task orchestration, structured workflows
   - Pattern: One agent coordinates others

2. **Handoffs**: Direct transfer between agents
   - Good for: Multi-domain conversations
   - Pattern: Agents hand off control to specialists

### Workflow Types

- **Sequential**: Linear flow, step-by-step
- **Parallel**: Concurrent execution
- **Cyclical**: Loops and iterations
- **Conditional**: Branching logic

## 📖 Documentation

### Official Resources

- [LangChain Python Docs](https://docs.langchain.com/oss/python/langchain/overview)
- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
- [Multi-Agent Guide](https://blog.langchain.com/langgraph-multi-agent-workflows)

### This Project

- `examples/`: Code examples with explanations
- `notebooks/`: Interactive learning notebooks
- `docs/`: Additional documentation (coming soon)

## 🔧 Configuration

### Required API Keys

```bash
# python/.env

OPENAI_API_KEY=sk-...  # Required for running agents
```

### Optional Configuration

```bash
# LangSmith for observability (highly recommended for learning)
LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY=ls-...
LANGCHAIN_PROJECT=espen-langchain-experiments

# Anthropic (for Claude models)
ANTHROPIC_API_KEY=sk-ant-...
```

### Get Your Keys

- **OpenAI**: [platform.openai.com](https://platform.openai.com/api-keys)
- **LangSmith**: [smith.langchain.com](https://smith.langchain.com/)
- **Anthropic**: [console.anthropic.com](https://console.anthropic.com/)

## 🎨 Visual Learning

This environment prioritizes visual understanding:

1. **Graph Diagrams**: See agent relationships
2. **Execution Traces**: Watch agents in action
3. **State Visualization**: Understand data flow
4. **Interactive Notebooks**: Experiment in real-time

### Viewing Visualizations

After running examples, check:
- `python/visualizations/` for generated graphs
- LangSmith UI for execution traces
- Jupyter notebooks for inline charts

## 🐛 Troubleshooting

### Import Errors

```bash
# Make sure you're in the virtual environment
source venv/bin/activate

# Verify installations
pip list | grep langchain
```

### API Key Issues

```bash
# Check your .env file
cat python/.env

# Test API keys
python python/notebooks/00_setup_and_overview.py
```

### Visualization Issues

```bash
# Install system graphviz (optional)
brew install graphviz  # macOS
# or
apt-get install graphviz  # Ubuntu/Debian
```

## 🤝 Contributing

This is a personal learning project, but suggestions welcome!

## 📝 License

MIT License - See LICENSE file

## 🙏 Acknowledgments

- [LangChain Team](https://github.com/langchain-ai)
- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
- All the open-source contributors

---

**Happy Building! 🚀**

*Questions? Check the examples first, then the official documentation.*

