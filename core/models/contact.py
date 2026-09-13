from __future__ import annotations

from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.database.base import Base
from core.models.mixins import UUIDMixin, UpdatedTimestampMixin

if TYPE_CHECKING:
    from core.models.company import Company
    from core.models.lead import Lead


class Contact(UUIDMixin, UpdatedTimestampMixin, Base):
    __tablename__ = "contacts"

    company_id: Mapped[UUID] = mapped_column(ForeignKey("companies.id", ondelete="CASCADE"), nullable=False, index=True)
    first_name: Mapped[str | None] = mapped_column(String(100), nullable=True)
    last_name: Mapped[str | None] = mapped_column(String(100), nullable=True)
    email: Mapped[str | None] = mapped_column(String(320), nullable=True, index=True)
    title: Mapped[str | None] = mapped_column(String(255), nullable=True)
    linkedin_url: Mapped[str | None] = mapped_column(String(500), nullable=True)

    company: Mapped[Company] = relationship(back_populates="contacts")
    leads: Mapped[list[Lead]] = relationship(back_populates="contact")
