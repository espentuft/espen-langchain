# 🚀 START HERE - Your Multi-Agent Learning Journey

Welcome to your **visual-first** learning environment for building multi-agent workflows with LangChain and LangGraph!

## 🎯 What You Have

A complete, curated learning environment optimized for:
- ✅ **Design leaders** who think visually
- ✅ **AI-native builders** who learn by doing
- ✅ **Fast exploration** of multi-agent concepts
- ✅ **Production-ready** patterns and practices

## ⚡ Choose Your Path

### 🏃 Quick Start (2 minutes)

Already have your OpenAI API key?

```bash
# 1. Configure API key
cp python/.env.example python/.env
# Edit python/.env with your key

# 2. Activate environment  
source venv/bin/activate

# 3. Run your first agent!
python python/examples/01_simple_agent.py
```

Done! You just ran your first agent 🎉

### 🎓 Follow the Learning Path (Recommended)

Prefer a structured approach?

1. **Start here**: `docs/QUICK_START.md` - Complete learning path
2. **Day 1**: Foundation with visual examples
3. **Day 2**: Real LangGraph implementation
4. **Day 3**: Customize and build your own

### 👀 Visual Explorer

Want to see what's possible before diving in?

```bash
# View visualizations (no API key needed)
python python/examples/02_multi_agent_graph.py
```

You'll see beautiful graph visualizations of multi-agent architectures!

## 📁 What's Inside

```
espen-langchain/
├── 📚 docs/
│   ├── QUICK_START.md          ← Start here for learning path
│   ├── LANGSMITH_SETUP.md      ← Visual debugging setup
│   └── SETUP.md                ← Detailed setup guide
│
├── 🐍 python/
│   ├── examples/
│   │   ├── 01_simple_agent.py              ← First agent (5 min)
│   │   ├── 02_multi_agent_graph.py         ← Visual learning (10 min)
│   │   └── 03_langgraph_real_multi_agent.py ← Real LangGraph (20 min)
│   │
│   └── notebooks/
│       ├── 00_setup_and_overview.py        ← Verify setup
│       └── 01_multi_agent_interactive.py   ← Interactive learning
│
└── 🖼️  python/visualizations/    ← Your generated graphs
```

## 🎨 Visual Learning Philosophy

This environment is built around **seeing is understanding**:

1. **See it**: Beautiful graph visualizations
2. **Try it**: Interactive examples
3. **Build it**: Copy and customize
4. **Debug it**: LangSmith observability

## 🎯 Key Multi-Agent Patterns

You'll learn two main patterns:

### Pattern 1: Tool Calling (Orchestration)
```
Supervisor → Researcher → Writer → Reviewer
```
Centralized control, specialized agents as tools.

### Pattern 2: Handoffs (Passing Control)
```
Researcher → Writer → Reviewer
```
Distributed decision-making, agent autonomy.

## 🛠️ Your Tools

| Tool | Purpose | Status |
|------|---------|--------|
| LangChain | LLM framework | ✅ Installed |
| LangGraph | Agent orchestration | ✅ Installed |
| LangSmith | Visual debugging | ✅ Installed |
| NetworkX | Graph visualization | ✅ Installed |
| Jupyter | Interactive learning | ✅ Installed |

## 📊 Example Outcomes

After completing the examples, you'll:

✅ Understand multi-agent architectures  
✅ Build LangGraph workflows  
✅ Visualize agent interactions  
✅ Debug with LangSmith  
✅ Create custom agents  
✅ Deploy production patterns  

## 🎓 Next Steps

### Immediate (5 min)
1. Run setup verification: `python python/notebooks/00_setup_and_overview.py`
2. View visualizations: `python python/examples/02_multi_agent_graph.py`

### This Week
1. Read: `docs/QUICK_START.md`
2. Run all examples
3. Setup LangSmith for debugging
4. Build your first custom workflow

### This Month
1. Explore advanced patterns
2. Integrate with your projects
3. Share learnings with team
4. Contribute back!

## 🌟 Recommended Order

```
Day 1: Foundation
├── docs/QUICK_START.md          (read)
├── examples/01_simple_agent.py  (run)
└── examples/02_multi_agent_graph.py (run)

Day 2: Real Implementation  
├── examples/03_langgraph_real_multi_agent.py (run)
├── docs/LANGSMITH_SETUP.md      (setup)
└── notebooks/01_multi_agent_interactive.py (explore)

Day 3: Customization
├── Modify agent prompts
├── Add your own tools
└── Build your first workflow
```

## 🆘 Need Help?

- **Setup issues**: Check `docs/SETUP.md`
- **Learning path**: See `docs/QUICK_START.md`
- **Debugging**: `docs/LANGSMITH_SETUP.md`
- **Code questions**: Read `python/README.md`
- **LangChain docs**: https://docs.langchain.com/oss/python/langchain/overview

## 🎉 Ready to Start?

```bash
# Verify everything works
source venv/bin/activate
python python/notebooks/00_setup_and_overview.py
```

Then pick your path above! 🚀

---

**Repository**: [github.com/espentuft/espen-langchain](https://github.com/espentuft/espen-langchain)

**Happy Learning! 🎓**

