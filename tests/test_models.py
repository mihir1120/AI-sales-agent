from core.database.base import Base
from core.models import (
    AgentRun,
    BuyingSignal,
    Company,
    Contact,
    Lead,
    LeadScore,
    Outreach,
    Research,
    ToolCall,
)


def test_all_v1_models_are_importable() -> None:
    assert all((Company, Contact, Lead, Research, BuyingSignal, LeadScore, Outreach, AgentRun, ToolCall))


def test_all_v1_tables_are_registered_in_metadata() -> None:
    expected = {
        "companies",
        "contacts",
        "leads",
        "research",
        "buying_signals",
        "lead_scores",
        "outreach",
        "agent_runs",
        "tool_calls",
    }
    assert expected == set(Base.metadata.tables)
