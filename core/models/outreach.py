from __future__ import annotations

from typing import Any, TYPE_CHECKING
from uuid import UUID

from sqlalchemy import Enum, ForeignKey, String, Text
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.database.base import Base
from core.models.enums import ApprovalStatus, OutreachStatus
from core.models.mixins import UUIDMixin, UpdatedTimestampMixin

if TYPE_CHECKING:
    from core.models.lead import Lead


class Outreach(UUIDMixin, UpdatedTimestampMixin, Base):
    __tablename__ = "outreach"

    lead_id: Mapped[UUID] = mapped_column(ForeignKey("leads.id", ondelete="CASCADE"), nullable=False, index=True)
    subject: Mapped[str | None] = mapped_column(String(500), nullable=True)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    status: Mapped[OutreachStatus] = mapped_column(Enum(OutreachStatus, name="outreach_status"), nullable=False, default=OutreachStatus.DRAFT, index=True)
    approval_status: Mapped[ApprovalStatus] = mapped_column(Enum(ApprovalStatus, name="approval_status"), nullable=False, default=ApprovalStatus.PENDING, index=True)
    structured_data: Mapped[dict[str, Any]] = mapped_column(JSONB, nullable=False, default=dict)

    lead: Mapped[Lead] = relationship(back_populates="outreach")
