import json

from agents import research


class FakeResponse:
    status = "completed"
    output_text = json.dumps(
        {
            "summary": "Example company research",
            "industry": "Software",
            "company_size": "51-200",
            "facts": ["The company provides B2B software."],
            "signals": [
                {
                    "signal_type": "Hiring",
                    "description": "The company is hiring for a role relevant to the product area.",
                    "source_url": "https://example.com/jobs",
                    "evidence": "A current job listing mentions the relevant function.",
                }
            ],
            "sources": [
                {"title": "Company jobs", "url": "https://example.com/jobs"}
            ],
        }
    )


class FakeResponses:
    def create(self, **kwargs):
        assert kwargs["tools"][0]["type"] == "web_search"
        return FakeResponse()


class FakeClient:
    def __init__(self, **kwargs):
        self.responses = FakeResponses()


def test_research_agent_returns_structured_result(monkeypatch):
    monkeypatch.setattr(research, "OpenAI", FakeClient)
    monkeypatch.setattr(
        research,
        "get_settings",
        lambda: type("Settings", (), {"openai_api_key": "test", "research_model": "test-model"})(),
    )

    result = research.run_research("Example Company", "https://example.com")

    assert result.industry == "Software"
    assert len(result.signals) == 1
    assert result.signals[0].signal_type == "Hiring"
