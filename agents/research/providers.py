from __future__ import annotations

from core.schemas.research import BuyingSignalResult, ResearchResult, ResearchSource


def run_mock_research(company_name: str, website: str | None = None) -> ResearchResult:
    source_url = website or "https://example.com"
    return ResearchResult(
        summary=f"Development research placeholder for {company_name}. Replace the mock provider with a live research provider before production use.",
        industry="Unknown",
        company_size=None,
        facts=[f"Company name: {company_name}"],
        signals=[
            BuyingSignalResult(
                signal_type="Development",
                description="Deterministic development signal used to verify buying-signal persistence.",
                source_url=source_url,
                evidence="Mock provider generated this signal for local integration testing.",
            )
        ],
        sources=[ResearchSource(title="Provided company website", url=source_url)],
    )
