# 🧠 Simple AI Research Agent

A basic Python-based AI research assistant using LangChain and OpenAI (or Anthropic) to search the web, summarize topics, and save notes to a file.

## 🚀 Features

- 🔍 Web search via DuckDuckGo
- 📚 Wikipedia summaries
- 🧾 Saves structured research summaries
- 🤖 Powered by OpenAI GPT-4o or Anthropic Claude
- 📄 Outputs in structured Pydantic format

## 📦 Requirements

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a .env file with your API keys:

```
OPENAI_API_KEY=your_openai_key
ANTHROPIC_API_KEY=your_anthropic_key  # optional if using Anthropic
```