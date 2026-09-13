from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from agents.research import run_research
from core.database.session import SessionLocal
from core.models.buying_signal import BuyingSignal
from core.models.company import Company
from core.models.research import Research
from core.schemas.research import ResearchRequest, ResearchResponse

router = APIRouter(prefix="/research", tags=["research"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("", response_model=ResearchResponse)
def research_company(request: ResearchRequest, db: Session = Depends(get_db)) -> ResearchResponse:
    try:
        result = run_research(request.company_name, str(request.website) if request.website else None)

        company = db.scalar(select(Company).where(Company.name == request.company_name))
        if company is None:
            company = Company(
                name=request.company_name,
                website=str(request.website) if request.website else None,
                industry=result.industry,
                company_size=result.company_size,
            )
            db.add(company)
            db.flush()
        else:
            if request.website:
                company.website = str(request.website)
            if result.industry:
                company.industry = result.industry
            if result.company_size:
                company.company_size = result.company_size

        research = Research(
            company_id=company.id,
            summary=result.summary,
            industry=result.industry,
            company_size=result.company_size,
            structured_data={"facts": result.facts, "signals": result.model_dump(mode="json")["signals"]},
            sources=result.model_dump(mode="json")["sources"],
        )
        db.add(research)

        for signal in result.signals:
            db.add(
                BuyingSignal(
                    company_id=company.id,
                    signal_type=signal.signal_type,
                    description=signal.description,
                    source=str(signal.source_url),
                    metadata_={"evidence": signal.evidence, "source_url": str(signal.source_url)},
                )
            )

        db.commit()
        db.refresh(research)
        return ResearchResponse(
            company_id=str(company.id),
            research_id=str(research.id),
            result=result,
        )
    except Exception as exc:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Research failed: {exc}") from exc
