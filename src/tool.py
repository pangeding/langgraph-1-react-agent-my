import os
from dotenv import load_dotenv
from langchain.tools import tool
from langchain_openai.chat_models import ChatOpenAI
from langchain_tavily import TavilySearch

load_dotenv()
DASHSCOPE_API_KEY = os.getenv("DASHSCOPE_API_KEY")
DASHSCOPE_BASE_URL = os.getenv("DASHSCOPE_BASE_URL")
DASHSCOPE_MODEL = os.getenv("DASHSCOPE_MODEL")


@tool
def triple(num: float) -> float:
    """
    :param num: a number to triple
    :return: the number tripled ->  multiplied by 3
    """
    print("triple is called")
    return num * 3


tools = [triple, TavilySearch(max_results=1)]

llm = ChatOpenAI(
    model=DASHSCOPE_MODEL,
    api_key=DASHSCOPE_API_KEY,
    base_url=DASHSCOPE_BASE_URL
).bind_tools(tools)
