from __future__ import annotations

from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.database.base import Base
from core.models.mixins import UUIDMixin, UpdatedTimestampMixin

if TYPE_CHECKING:
    from core.models.buying_signal import BuyingSignal
    from core.models.contact import Contact
    from core.models.lead import Lead
    from core.models.research import Research


class Company(UUIDMixin, UpdatedTimestampMixin, Base):
    __tablename__ = "companies"

    name: Mapped[str] = mapped_column(String(255), nullable=False, index=True)
    website: Mapped[str | None] = mapped_column(String(500), nullable=True)
    industry: Mapped[str | None] = mapped_column(String(255), nullable=True, index=True)
    company_size: Mapped[str | None] = mapped_column(String(100), nullable=True)

    contacts: Mapped[list[Contact]] = relationship(back_populates="company", cascade="all, delete-orphan")
    leads: Mapped[list[Lead]] = relationship(back_populates="company", cascade="all, delete-orphan")
    research: Mapped[list[Research]] = relationship(back_populates="company", cascade="all, delete-orphan")
    buying_signals: Mapped[list[BuyingSignal]] = relationship(back_populates="company")
