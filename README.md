# LangGraph React Course

A Python project for learning LangGraph with React integration.

## Description

This is a course project that demonstrates how to use LangGraph with React.

## Installation

Using uv:

```bash
uv sync
```

## Usage

### Traditional Usage

```bash
python src/main.py
```

### Development with LangGraph Studio

Install langgraph-cli:
```bash
uv pip install -U langgraph-cli
```
删除 uv.lock 重新 uv sync
Start development server:
```bash
langgraph dev
```

Then open your browser and visit: `http://localhost:54367`

You can also specify a custom port or enable hot-reload:
```bash
langgraph dev --port 8000
langgraph dev --reload
```

## Dependencies

- langchain
- langgraph
- langchain-openai
- langchainhub
- black
- isort
- python-dotenv
- langchain-tavily

## License

MIT
