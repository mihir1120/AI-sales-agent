from __future__ import annotations

from typing import Any, TYPE_CHECKING
from uuid import UUID

from sqlalchemy import Enum, ForeignKey, String
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.database.base import Base
from core.models.enums import ToolCallStatus
from core.models.mixins import UUIDMixin, TimestampMixin

if TYPE_CHECKING:
    from core.models.agent_run import AgentRun


class ToolCall(UUIDMixin, TimestampMixin, Base):
    __tablename__ = "tool_calls"

    agent_run_id: Mapped[UUID | None] = mapped_column(ForeignKey("agent_runs.id", ondelete="CASCADE"), nullable=True, index=True)
    tool_name: Mapped[str] = mapped_column(String(255), nullable=False, index=True)
    status: Mapped[ToolCallStatus] = mapped_column(Enum(ToolCallStatus, name="tool_call_status"), nullable=False, default=ToolCallStatus.STARTED, index=True)
    input: Mapped[dict[str, Any]] = mapped_column(JSONB, nullable=False, default=dict)
    output: Mapped[dict[str, Any]] = mapped_column(JSONB, nullable=False, default=dict)

    agent_run: Mapped[AgentRun | None] = relationship(back_populates="tool_calls")
