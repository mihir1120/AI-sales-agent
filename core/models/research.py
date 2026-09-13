from __future__ import annotations

from typing import Any, TYPE_CHECKING
from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Text, String

from core.database.base import Base
from core.models.mixins import UUIDMixin, TimestampMixin

if TYPE_CHECKING:
    from core.models.company import Company


class Research(UUIDMixin, TimestampMixin, Base):
    __tablename__ = "research"

    company_id: Mapped[UUID] = mapped_column(ForeignKey("companies.id", ondelete="CASCADE"), nullable=False, index=True)
    summary: Mapped[str] = mapped_column(Text, nullable=False)
    industry: Mapped[str | None] = mapped_column(String(255), nullable=True)
    company_size: Mapped[str | None] = mapped_column(String(100), nullable=True)
    structured_data: Mapped[dict[str, Any]] = mapped_column(JSONB, nullable=False, default=dict)
    sources: Mapped[list[Any]] = mapped_column(JSONB, nullable=False, default=list)

    company: Mapped[Company] = relationship(back_populates="research")
