from dotenv import load_dotenv

from langgraph.graph import END, MessagesState, StateGraph
from langchain_core.messages import HumanMessage

load_dotenv()

LAST = -1

flow = StateGraph(MessagesState)

app = flow.compile()

if __name__ == "__main__":
    print("Hello ReAct with LangGraph")
    res = app.invoke(
        {
            "messages": [
                HumanMessage(
                    content="What is the weather in Beijing? List it and triple it."
                )
            ]
        }
    )
    print(res["messages"][LAST].content)
