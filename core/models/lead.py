from __future__ import annotations

from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import Enum, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.database.base import Base
from core.models.enums import LeadStatus
from core.models.mixins import UUIDMixin, UpdatedTimestampMixin

if TYPE_CHECKING:
    from core.models.buying_signal import BuyingSignal
    from core.models.company import Company
    from core.models.contact import Contact
    from core.models.lead_score import LeadScore
    from core.models.outreach import Outreach


class Lead(UUIDMixin, UpdatedTimestampMixin, Base):
    __tablename__ = "leads"

    company_id: Mapped[UUID] = mapped_column(ForeignKey("companies.id", ondelete="CASCADE"), nullable=False, index=True)
    contact_id: Mapped[UUID | None] = mapped_column(ForeignKey("contacts.id", ondelete="SET NULL"), nullable=True, index=True)
    status: Mapped[LeadStatus] = mapped_column(Enum(LeadStatus, name="lead_status"), nullable=False, default=LeadStatus.NEW, index=True)
    source: Mapped[str | None] = mapped_column(String(255), nullable=True)

    company: Mapped[Company] = relationship(back_populates="leads")
    contact: Mapped[Contact | None] = relationship(back_populates="leads")
    buying_signals: Mapped[list[BuyingSignal]] = relationship(back_populates="lead")
    scores: Mapped[list[LeadScore]] = relationship(back_populates="lead", cascade="all, delete-orphan")
    outreach: Mapped[list[Outreach]] = relationship(back_populates="lead", cascade="all, delete-orphan")
