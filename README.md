# Espen LangChain

A **visual-first** learning environment for building multi-agent workflows with [LangChain](https://docs.langchain.com/oss/python/langchain/overview) and LangGraph, optimized for design leaders and AI-native builders.

## 🚀 Quick Start

**👋 NEW?** Read [`START_HERE.md`](START_HERE.md) first!

This project uses **Python** for multi-agent workflows and learning. Node.js setup is available but Python is recommended for LangGraph.

### Python Setup (Recommended)

```bash
# 1. Activate virtual environment
source venv/bin/activate

# 2. Configure API keys
cp python/.env.example python/.env
# Edit python/.env with your OpenAI API key

# 3. Run your first example
python python/examples/01_simple_agent.py

# 4. Launch interactive learning
jupyter lab python/notebooks/
```

### Node.js Setup (Available)

```bash
# Install dependencies
npm install

# Run starter
npm run dev
```

## 📁 Project Structure

```
espen-langchain/
├── python/                    # 🐍 Python learning environment (Recommended)
│   ├── examples/              # Runnable examples
│   │   ├── 01_simple_agent.py              # Basic agent setup
│   │   ├── 02_multi_agent_graph.py         # Visual multi-agent patterns
│   │   └── 03_langgraph_real_multi_agent.py # Real LangGraph implementation
│   ├── notebooks/             # Interactive Jupyter notebooks
│   │   ├── 00_setup_and_overview.py       # Setup verification
│   │   └── 01_multi_agent_interactive.py  # Interactive learning
│   ├── agents/                # Reusable agent implementations
│   ├── visualizations/        # Generated graphs and charts
│   └── README.md             # Detailed Python learning guide
│
├── docs/                      # 📚 Documentation
│   ├── QUICK_START.md        # Complete learning path
│   ├── LANGSMITH_SETUP.md    # Observability setup
│   └── SETUP.md              # Detailed setup
├── src/                       # 📦 Node.js source (Optional)
├── venv/                      # Python virtual environment
├── requirements.txt           # Python dependencies
└── START_HERE.md             # 👋 Start your journey here!

```

## 🎯 Learning Path

### Python (Recommended for LangGraph)

1. **Setup**: Activate venv and configure API keys
2. **Simple Agent**: Run `python python/examples/01_simple_agent.py`
3. **Multi-Agent**: Run `python python/examples/02_multi_agent_graph.py`
4. **Real LangGraph**: Run `python python/examples/03_langgraph_real_multi_agent.py`
5. **Interactive**: Launch Jupyter Lab for hands-on exploration

### Key Resources

- 🚀 [START_HERE.md](START_HERE.md) - **Begin your journey here!**
- 📖 [Quick Start Guide](docs/QUICK_START.md) - Complete learning path
- 📚 [Python README](python/README.md) - Detailed Python learning guide
- 🔍 [LangSmith Setup](docs/LANGSMITH_SETUP.md) - Visual debugging
- 🔗 [LangChain Docs](https://docs.langchain.com/oss/python/langchain/overview)
- 🎨 [Multi-Agent Guide](https://blog.langchain.com/langgraph-multi-agent-workflows)

## 🛠️ Technologies

### Core

- **LangChain**: Framework for LLM applications
- **LangGraph**: Graph-based agent orchestration
- **Python 3.9+**: Primary language for agent development
- **OpenAI GPT**: LLM provider

### Visualization & Learning

- **Jupyter Lab**: Interactive notebooks
- **Matplotlib**: Graphs and charts
- **NetworkX**: Graph structures
- **LangSmith**: Observability and debugging

## 🎓 What You'll Learn

- ✅ Creating agents with LangChain
- ✅ Multi-agent collaboration patterns
- ✅ Graph-based workflow visualization
- ✅ Tool integration and orchestration
- ✅ Debugging with LangSmith
- ✅ Production patterns and best practices

## 📚 Additional Documentation

- `START_HERE.md` - **👋 Start your journey**
- `docs/QUICK_START.md` - Complete learning path
- `docs/LANGSMITH_SETUP.md` - Visual debugging setup
- `python/README.md` - Detailed Python learning guide
- `docs/SETUP.md` - Detailed setup instructions
- `GIT_SETUP.md` - Git and GitHub setup
- `PROJECT_INFO.md` - Project information

## 🤝 Repository

- **GitHub**: https://github.com/espentuft/espen-langchain
- **Local**: `/Users/espentuft/Documents/production/espen-langchain`

---

**Happy Building! 🚀**

