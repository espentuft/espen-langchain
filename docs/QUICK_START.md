# Quick Start Guide - Multi-Agent Learning

Welcome! This guide will get you exploring multi-agent workflows in **under 5 minutes**.

## ⚡ Super Quick Start (No API Key Needed)

Even without API keys, you can explore the visualizations:

```bash
# 1. Activate environment
source venv/bin/activate

# 2. View existing visualizations
ls python/visualizations/

# 3. Explore the examples (runs mocked without API)
python python/examples/02_multi_agent_graph.py
```

You'll see:
- 📊 Beautiful graph visualizations
- 🎨 Agent workflow diagrams  
- 💡 Learning patterns explained

## 🚀 Full Setup (With API Key)

### Step 1: Configure API Key

Edit `python/.env`:
```bash
OPENAI_API_KEY=sk-your-actual-key-here
```

### Step 2: Verify Setup

```bash
python python/notebooks/00_setup_and_overview.py
```

Expected output:
```
✅ LangChain: 0.3.x
✅ LangGraph installed
✅ OpenAI API key configured
```

### Step 3: Run Your First Real Agent

```bash
python python/examples/01_simple_agent.py
```

You'll see a complete agent conversation!

### Step 4: Explore Multi-Agent Workflows

```bash
# Visual workflow demonstration
python python/examples/02_multi_agent_graph.py

# Real LangGraph implementation
python python/examples/03_langgraph_real_multi_agent.py
```

## 🎓 Recommended Learning Path

### Day 1: Foundations
1. ✅ Run `00_setup_and_overview.py` - Verify everything works
2. 🤖 Run `01_simple_agent.py` - Understand basic agents
3. 📊 Run `02_multi_agent_graph.py` - See visual workflows

### Day 2: Real Implementation
4. 🔧 Run `03_langgraph_real_multi_agent.py` - Build real LangGraph
5. 📓 Launch `01_multi_agent_interactive.py` - Interactive learning
6. 🔍 Setup LangSmith - Visual debugging (see `LANGSMITH_SETUP.md`)

### Day 3: Customization
7. ✏️ Modify agent prompts in the examples
8. 🔨 Add your own tools
9. 🎨 Build your first custom workflow

## 🎨 Visual Learning Features

This environment maximizes visual understanding:

### Graph Visualizations
- See agent relationships
- Understand data flow
- Identify bottlenecks

### Workflow Diagrams  
- Mermaid diagrams for architecture
- PNG exports for presentations
- Interactive exploration

### LangSmith Integration
- Real-time debugging
- Execution traces
- Performance metrics

## 📚 Learning Resources

| Resource | Purpose | When to Use |
|----------|---------|-------------|
| `examples/01_simple_agent.py` | Basic agent concepts | First day |
| `examples/02_multi_agent_graph.py` | Visual patterns | Day 1 |
| `examples/03_langgraph_real_multi_agent.py` | Real implementation | Day 2+ |
| `notebooks/00_setup_and_overview.py` | Environment check | Start here |
| `notebooks/01_multi_agent_interactive.py` | Hands-on learning | Day 2+ |
| `docs/LANGSMITH_SETUP.md` | Observability | Day 2+ |
| `docs/SETUP.md` | Detailed setup | Reference |

## 🛠️ Common Commands

```bash
# Activate environment
source venv/bin/activate

# Run any example
python python/examples/01_simple_agent.py

# Start Jupyter for interactive learning
jupyter lab python/notebooks/

# Check setup
python python/notebooks/00_setup_and_overview.py

# View visualizations
open python/visualizations/
```

## 🎯 Key Concepts You'll Learn

### Multi-Agent Patterns

1. **Tool Calling Pattern**
   - Supervisor orchestrates specialists
   - Centralized control
   - Good for structured workflows

2. **Handoff Pattern**
   - Agents pass control directly
   - Distributed decision-making
   - Good for conversations

3. **Hybrid Patterns**
   - Combine both approaches
   - Maximum flexibility
   - Production patterns

### LangGraph Concepts

- **StateGraph**: Define your workflow
- **Nodes**: Individual agents or functions
- **Edges**: Connections between nodes
- **State**: Shared data between agents
- **Routing**: Conditional flow logic

## 🐛 Troubleshooting

### "Module not found"

```bash
# Make sure you're in the venv
source venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

### "API key not configured"

```bash
# Check your .env file
cat python/.env

# Make sure it has your actual key
```

### "No visualization generated"

```bash
# Install networkx if missing
pip install networkx

# Check visualization directory exists
mkdir -p python/visualizations
```

## 🎉 You're Ready!

Start with any example and explore:

```bash
python python/examples/01_simple_agent.py
```

**Questions?** Check:
- `python/README.md` - Detailed Python guide
- `docs/SETUP.md` - Complete setup instructions  
- Official docs: https://docs.langchain.com/oss/python/langchain/overview

**Happy Learning! 🚀**

