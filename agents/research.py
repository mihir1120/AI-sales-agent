from __future__ import annotations

import json
from typing import TypedDict

from langgraph.graph import END, START, StateGraph
from openai import OpenAI

from core.config.settings import get_settings
from core.schemas.research import ResearchResult


RESEARCH_PROMPT = """
You are the Research Agent for a B2B sales system.

Research the target company using current public web information.
Return ONLY valid JSON matching this exact shape:
{
  "summary": "string",
  "industry": "string or null",
  "company_size": "string or null",
  "facts": ["short fact with source URL", "..."],
  "signals": [
    {
      "signal_type": "string",
      "description": "why this may matter for sales",
      "source_url": "https://...",
      "evidence": "specific evidence"
    }
  ],
  "sources": [
    {"title": "source title", "url": "https://..."}
  ]
}

Rules:
- Use current public information and search the web before answering.
- Prefer primary/company sources and reputable business/news sources.
- Do not invent facts, people, funding, hiring, products, or buying intent.
- A buying signal must have concrete evidence and a source URL.
- It is acceptable to return zero signals.
- Keep the summary concise and useful to a salesperson.
- Every source URL must be a real URL returned by web research.
"""


class ResearchState(TypedDict, total=False):
    company_name: str
    website: str | None
    result: ResearchResult


def _research_node(state: ResearchState) -> ResearchState:
    settings = get_settings()
    if not settings.openai_api_key:
        raise RuntimeError("OPENAI_API_KEY is not configured")

    client = OpenAI(api_key=settings.openai_api_key)
    target = f"Company: {state['company_name']}"
    if state.get("website"):
        target += f"\nWebsite: {state['website']}"

    response = client.responses.create(
        model=settings.research_model,
        tools=[{"type": "web_search", "search_context_size": "medium"}],
        input=[
            {"role": "system", "content": RESEARCH_PROMPT},
            {"role": "user", "content": target},
        ],
        text={"format": {"type": "json_object"}},
    )

    if response.status != "completed":
        raise RuntimeError(f"Research response incomplete: {response.status}")

    result = ResearchResult.model_validate(json.loads(response.output_text))
    return {**state, "result": result}


def build_research_graph():
    graph = StateGraph(ResearchState)
    graph.add_node("research", _research_node)
    graph.add_edge(START, "research")
    graph.add_edge("research", END)
    return graph.compile()


def run_research(company_name: str, website: str | None = None) -> ResearchResult:
    result = build_research_graph().invoke(
        {"company_name": company_name, "website": website}
    )
    return result["result"]
