from enum import StrEnum


class LeadStatus(StrEnum):
    NEW = "new"
    RESEARCHED = "researched"
    QUALIFIED = "qualified"
    DISQUALIFIED = "disqualified"


class LeadScoreClassification(StrEnum):
    HOT = "hot"
    WARM = "warm"
    COLD = "cold"
    REJECT = "reject"


class OutreachStatus(StrEnum):
    DRAFT = "draft"
    READY_FOR_APPROVAL = "ready_for_approval"
    APPROVED = "approved"
    REJECTED = "rejected"


class ApprovalStatus(StrEnum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"


class AgentRunStatus(StrEnum):
    STARTED = "started"
    COMPLETED = "completed"
    FAILED = "failed"


class ToolCallStatus(StrEnum):
    STARTED = "started"
    COMPLETED = "completed"
    FAILED = "failed"
