# Setup Instructions

## Initial Setup

1. **Install dependencies:**
   ```bash
   npm install
   ```

2. **Set up environment variables:**
   Create a `.env` file in the root directory:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   # Add other API keys as needed
   ```

3. **Run the starter application:**
   ```bash
   npm run dev
   ```

## LangChain Setup

### JavaScript/TypeScript

1. Install LangChain packages as needed:
   ```bash
   npm install langchain @langchain/core
   npm install @langchain/openai  # for OpenAI
   npm install @langchain/anthropic  # for Claude
   ```

2. Import and use in your code:
   ```javascript
   import { ChatOpenAI } from "@langchain/openai";
   ```

### Python (Alternative)

If you prefer Python:
```bash
pip install langchain
pip install langchain-openai
pip install python-dotenv
```

## Getting Started

1. Start with simple chains
2. Experiment with prompts
3. Build agents
4. Integrate tools
5. Add vector stores for document processing

## Resources

- [LangChain Documentation](https://js.langchain.com/)
- [LangChain Cookbook](https://cookbook.langchain.com/)
- [LangChain Examples](https://github.com/langchain-ai/langchainjs/tree/main/examples)

