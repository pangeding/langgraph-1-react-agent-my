from dotenv import load_dotenv

from langchain_core.messages import HumanMessage

from src.graph import graph
from src.constant import LAST
# 加载 .env 文件（从当前文件所在目录）
load_dotenv()


LAST = -1

if __name__ == "__main__":
    print("Hello ReAct with LangGraph")
    res = graph.invoke(
        {
            "messages": [
                HumanMessage(
                    content="What is the weather in Beijing? List it and triple it."
                )
            ]
        }
    )
    print(res["messages"][LAST].content)
