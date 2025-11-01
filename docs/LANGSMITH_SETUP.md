# LangSmith Setup for Visual Learning

**LangSmith** is a powerful observability platform that lets you **see** your agents in action. It's like a debugger for LLM applications, providing visual traces of agent execution.

## 🎯 Why Use LangSmith?

As a design leader and AI-native builder, you'll love:
- **Visual agent traces**: See exactly what each agent does
- **Performance metrics**: Track latency, costs, tokens used
- **Error debugging**: Quickly find where things go wrong
- **Experimentation**: Compare different agent configurations side-by-side

## 🚀 Quick Setup

### 1. Get Your LangSmith API Key

1. Go to [smith.langchain.com](https://smith.langchain.com/)
2. Sign up or log in
3. Navigate to **Settings** → **API Keys**
4. Create a new API key
5. Copy the key (starts with `ls_`)

### 2. Configure Environment

Add to your `python/.env` file:

```bash
# LangSmith Configuration
LANGCHAIN_TRACING_V2=true
LANGCHAIN_ENDPOINT=https://api.smith.langchain.com
LANGCHAIN_API_KEY=ls_your_key_here
LANGCHAIN_PROJECT=espen-langchain-experiments

# Optional: Enable verbose logging
LANGCHAIN_VERBOSE=false
```

### 3. Test the Connection

Run the setup verification:

```bash
python python/notebooks/00_setup_and_overview.py
```

You should see:
```
✅ LangSmith API key configured (observability enabled)
```

## 🎨 What You'll See in LangSmith

### Agent Traces

Each time you run an agent, LangSmith records:
- **Input messages**: What the agent received
- **LLM calls**: Model interactions and parameters
- **Tool calls**: Functions the agent executed
- **Output**: Final responses
- **Timing**: How long each step took
- **Token usage**: Cost tracking

### Visual Workflow Diagrams

LangSmith automatically creates visual diagrams showing:
- Agent execution flow
- State transitions
- Decision points
- Parallel execution
- Errors and retries

## 📊 Using LangSmith in Your Learning

### Basic Usage

Once configured, LangSmith automatically traces all LangChain operations:

```python
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini")

# This will automatically be traced in LangSmith!
response = llm.invoke("Hello, world!")
```

### Viewing Traces

1. Run any of the examples:
   ```bash
   python python/examples/03_langgraph_real_multi_agent.py
   ```

2. Open LangSmith dashboard:
   - Go to [smith.langchain.com](https://smith.langchain.com/)
   - Click on your project: **espen-langchain-experiments**
   - See your traces appear in real-time!

3. Click on any trace to see:
   - Full execution timeline
   - Agent interactions
   - Tool calls
   - Inputs/outputs
   - Errors (if any)

### Comparing Experiments

Want to compare different configurations?

```bash
# Run experiment 1
LANGCHAIN_PROJECT=experiment-gpt4 python examples/01_simple_agent.py

# Run experiment 2
LANGCHAIN_PROJECT=experiment-gpt3 python examples/01_simple_agent.py

# Compare in LangSmith UI
```

## 🔍 Debugging Multi-Agent Workflows

LangSmith is especially powerful for multi-agent systems:

### 1. Identify Which Agent is Slow

In LangSmith, you can see:
- Which agent took the most time
- How agents interact
- Where bottlenecks occur

### 2. Track State Changes

See how state flows through your workflow:
- **Node**: Which agent acted
- **Input**: What the agent received
- **Output**: What the agent produced
- **Next**: Where the workflow went

### 3. Debug Failures

When something goes wrong:
- Click on the error in LangSmith
- See the exact input that caused it
- View the agent's reasoning
- Adjust and retry

## 🎓 Learning Exercises

### Exercise 1: Visual Trace Exploration

1. Run the simple agent example
2. Open LangSmith
3. Click through each trace
4. Identify:
   - How many LLM calls happened
   - What tools were called
   - Total time and cost

### Exercise 2: Multi-Agent Comparison

1. Run different workflow examples
2. In LangSmith, compare:
   - Which workflow was fastest?
   - Which used more tokens?
   - Which produced better outputs?

### Exercise 3: Debug a Custom Agent

1. Create a custom agent with a bug
2. Run it and check LangSmith
3. Use the trace to find the issue
4. Fix it and verify in LangSmith

## 💡 Pro Tips

### Organize Your Experiments

Use different projects for different learning goals:

```bash
# Learning basics
LANGCHAIN_PROJECT=langchain-basics python examples/01_simple_agent.py

# Multi-agent exploration
LANGCHAIN_PROJECT=multi-agent-research python examples/03_langgraph_real_multi_agent.py

# Custom experiments
LANGCHAIN_PROJECT=my-experiments python your_script.py
```

### Add Metadata

Tag your traces with useful information:

```python
from langchain_core.messages import HumanMessage

# Add metadata to help organize in LangSmith
msg = HumanMessage(
    content="Your query here",
    metadata={"experiment": "temperature-0.7", "agent": "research"}
)
```

### Enable Verbose Mode

For detailed debugging:

```bash
LANGCHAIN_VERBOSE=true python examples/03_langgraph_real_multi_agent.py
```

## 🐛 Troubleshooting

### No Traces Appearing?

1. Check your API key is correct
2. Verify `LANGCHAIN_TRACING_V2=true`
3. Make sure you're running with the venv activated:
   ```bash
   source venv/bin/activate
   ```
4. Check your project name matches in LangSmith

### SSL Errors?

If you see SSL certificate errors:
```bash
# Install certifi
pip install certifi

# Set environment variable
export SSL_CERT_FILE=$(python -m certifi)
```

### Rate Limiting?

LangSmith has generous free tiers, but if you hit limits:
- Slow down your experiments
- Use `.compile(checkpointer=)` for testing
- Consider upgrading your plan

## 📚 Additional Resources

- **LangSmith Docs**: [docs.smith.langchain.com](https://docs.smith.langchain.com/)
- **Tracing Guide**: [How to Use LangSmith for Tracing](https://docs.smith.langchain.com/tracing)
- **Video Tutorial**: [LangSmith Crash Course](https://youtube.com/watch?v=YourVideoID)

## 🎉 You're All Set!

Now you have a powerful visual debugging tool for your multi-agent learning journey.

**Next**: Run an example and watch it come alive in LangSmith!

```bash
python python/examples/03_langgraph_real_multi_agent.py
```

Then open: [smith.langchain.com](https://smith.langchain.com/)

---

**Happy Tracing! 🔍🚀**

