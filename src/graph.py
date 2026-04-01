from dotenv import load_dotenv

from langgraph.graph import END, MessagesState, StateGraph


from node import run_agent_reasoning_engine, tool_node

from constant import LAST

load_dotenv()



AGENT_REASON = "agent_reason"
ACT = "act"


def should_continue(state: dict) -> str:
    if not state["messages"][LAST].tool_calls:
        return END
    return ACT

flow = StateGraph(MessagesState)

flow.add_node(AGENT_REASON, run_agent_reasoning_engine)
flow.set_entry_point(AGENT_REASON)
flow.add_node(ACT, tool_node)

flow.add_conditional_edges(
    AGENT_REASON,
    should_continue,
    {
        END: END,
        ACT: ACT,
    },
)

flow.add_edge(ACT, AGENT_REASON)


graph = flow.compile()
graph.get_graph().draw_mermaid_png(output_file_path="graph.png")