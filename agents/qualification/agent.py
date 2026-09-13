from agents.orchestrator.state import SalesAgentState


def run_qualification_agent(state: SalesAgentState) -> SalesAgentState:
    result = {
        "agent": "qualification",
        "qualified": False,
        "reason": "Qualification criteria are not configured yet.",
    }

    return {
        **state,
        "result": result,
        "messages": [*state.get("messages", []), "qualification:completed"],
    }
