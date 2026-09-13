from __future__ import annotations

from pydantic import BaseModel, Field, HttpUrl


class ResearchRequest(BaseModel):
    company_name: str = Field(min_length=1, max_length=255)
    website: HttpUrl | None = None


class ResearchSource(BaseModel):
    title: str
    url: HttpUrl


class BuyingSignalResult(BaseModel):
    signal_type: str
    description: str
    source_url: HttpUrl
    evidence: str


class ResearchResult(BaseModel):
    summary: str
    industry: str | None = None
    company_size: str | None = None
    facts: list[str] = Field(default_factory=list)
    signals: list[BuyingSignalResult] = Field(default_factory=list)
    sources: list[ResearchSource] = Field(default_factory=list)


class ResearchResponse(BaseModel):
    company_id: str
    research_id: str
    result: ResearchResult
