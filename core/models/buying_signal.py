from __future__ import annotations

from typing import Any, TYPE_CHECKING
from uuid import UUID

from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.database.base import Base
from core.models.mixins import UUIDMixin, TimestampMixin

if TYPE_CHECKING:
    from core.models.company import Company
    from core.models.lead import Lead


class BuyingSignal(UUIDMixin, TimestampMixin, Base):
    __tablename__ = "buying_signals"

    company_id: Mapped[UUID | None] = mapped_column(ForeignKey("companies.id", ondelete="CASCADE"), nullable=True, index=True)
    lead_id: Mapped[UUID | None] = mapped_column(ForeignKey("leads.id", ondelete="CASCADE"), nullable=True, index=True)
    signal_type: Mapped[str] = mapped_column(String(100), nullable=False, index=True)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    source: Mapped[str | None] = mapped_column(String(500), nullable=True)
    metadata_: Mapped[dict[str, Any]] = mapped_column("metadata", JSONB, nullable=False, default=dict)

    company: Mapped[Company | None] = relationship(back_populates="buying_signals")
    lead: Mapped[Lead | None] = relationship(back_populates="buying_signals")
