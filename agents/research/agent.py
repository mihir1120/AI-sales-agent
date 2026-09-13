from agents.orchestrator.state import SalesAgentState


def run_research_agent(state: SalesAgentState) -> SalesAgentState:
    company_name = state.get("company_name", "Unknown Company")
    result = {
        "agent": "research",
        "company_name": company_name,
        "summary": "Research agent foundation is ready.",
        "sources": [],
    }

    return {
        **state,
        "result": result,
        "messages": [*state.get("messages", []), "research:completed"],
    }
