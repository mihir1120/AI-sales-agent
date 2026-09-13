from agents.orchestrator.state import SalesAgentState


def run_outreach_agent(state: SalesAgentState) -> SalesAgentState:
    result = {
        "agent": "outreach",
        "draft": None,
        "requires_human_approval": True,
    }

    return {
        **state,
        "result": result,
        "messages": [*state.get("messages", []), "outreach:completed"],
    }
