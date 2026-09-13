from langgraph.graph import END, START, StateGraph

from agents.orchestrator.state import SalesAgentState
from agents.qualification.agent import run_qualification_agent
from agents.outreach.agent import run_outreach_agent
from agents.research.agent import run_research_agent


def run_orchestrator(state: SalesAgentState) -> SalesAgentState:
    requested_action = state.get("requested_action", "research")
    if requested_action not in {"research", "qualification", "outreach"}:
        requested_action = "research"

    return {
        **state,
        "next_agent": requested_action,
        "messages": [*state.get("messages", []), "orchestrator:routed"],
    }


def select_next_agent(state: SalesAgentState) -> str:
    return state.get("next_agent", "research")


def create_sales_graph():
    graph = StateGraph(SalesAgentState)
    graph.add_node("orchestrator", run_orchestrator)
    graph.add_node("research", run_research_agent)
    graph.add_node("qualification", run_qualification_agent)
    graph.add_node("outreach", run_outreach_agent)

    graph.add_edge(START, "orchestrator")
    graph.add_conditional_edges(
        "orchestrator",
        select_next_agent,
        {
            "research": "research",
            "qualification": "qualification",
            "outreach": "outreach",
        },
    )
    graph.add_edge("research", END)
    graph.add_edge("qualification", END)
    graph.add_edge("outreach", END)

    return graph.compile()
