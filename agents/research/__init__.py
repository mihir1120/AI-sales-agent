from __future__ import annotations

import json

from openai import OpenAI

from core.config.settings import get_settings
from core.schemas.research import ResearchResult


def run_research(company_name: str, website: str | None = None) -> ResearchResult:
    settings = get_settings()
    if not settings.openai_api_key:
        raise ValueError("OPENAI_API_KEY is not configured")

    client = OpenAI(api_key=settings.openai_api_key)
    website_context = f"\nKnown website: {website}" if website else ""
    prompt = f"""Research the company below for a B2B sales team.

Company: {company_name}{website_context}

Use web search and return ONLY valid JSON matching this shape:
{{
  "summary": "...",
  "industry": "... or null",
  "company_size": "... or null",
  "facts": ["..."],
  "signals": [
    {{
      "signal_type": "...",
      "description": "...",
      "source_url": "https://...",
      "evidence": "..."
    }}
  ],
  "sources": [
    {{"title": "...", "url": "https://..."}}
  ]
}}

Focus on factual, sales-relevant information and current buying signals such as hiring,
product launches, expansion, funding, partnerships, technology changes, or leadership changes.
Do not invent facts. Prefer primary sources when available.
"""

    response = client.responses.create(
        model=settings.research_model,
        tools=[{"type": "web_search"}],
        input=prompt,
    )

    if getattr(response, "status", None) != "completed":
        raise RuntimeError(f"Research response did not complete: {getattr(response, 'status', 'unknown')}")

    raw = response.output_text.strip()
    if raw.startswith("```"):
        raw = raw.split("\n", 1)[1].rsplit("```", 1)[0].strip()

    try:
        payload = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise RuntimeError("Research model returned invalid JSON") from exc

    return ResearchResult.model_validate(payload)


from agents.research.agent import run_research_agent

__all__ = ["run_research", "run_research_agent", "OpenAI"]
