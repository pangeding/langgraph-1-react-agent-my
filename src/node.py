from dotenv import load_dotenv

from langgraph.graph import MessagesState
from langgraph.prebuilt import ToolNode

from react import tools, llm
load_dotenv()


SYSTEM_MESSAGE = """
    You are a helpful assistant.
"""

def run_agent_reasoning_engine(state: MessagesState) -> MessagesState:
    response = llm.invoke(
        [{"role": "system", "content": SYSTEM_MESSAGE}, *state["messages"]]
    )

    return {"messages": [response]}


tool_node = ToolNode(tools=tools)