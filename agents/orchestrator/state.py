from typing import Any, TypedDict


class SalesAgentState(TypedDict, total=False):
    requested_action: str
    company_name: str
    next_agent: str
    result: dict[str, Any]
    messages: list[str]
