from __future__ import annotations

from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import CheckConstraint, Enum, ForeignKey, Integer, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.database.base import Base
from core.models.enums import LeadScoreClassification
from core.models.mixins import UUIDMixin, TimestampMixin

if TYPE_CHECKING:
    from core.models.lead import Lead


class LeadScore(UUIDMixin, TimestampMixin, Base):
    __tablename__ = "lead_scores"
    __table_args__ = (CheckConstraint("score >= 0 AND score <= 100", name="ck_lead_scores_score_range"),)

    lead_id: Mapped[UUID] = mapped_column(ForeignKey("leads.id", ondelete="CASCADE"), nullable=False, index=True)
    score: Mapped[int] = mapped_column(Integer, nullable=False)
    classification: Mapped[LeadScoreClassification] = mapped_column(
        Enum(LeadScoreClassification, name="lead_score_classification"), nullable=False
    )
    explanation: Mapped[str] = mapped_column(Text, nullable=False)

    lead: Mapped[Lead] = relationship(back_populates="scores")
