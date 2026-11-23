"""Versioned workflow contracts; importing this module has no runtime effects."""
from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any
import uuid


class InputOrigin(str, Enum):
    USER = "user"
    WHATSAPP = "whatsapp"
    AUTONOMOUS = "autonomous"
    PROACTIVE = "proactive"
    TOOL = "tool"
    WEB = "web"
    OCR = "ocr"
    SUBAGENT = "subagent"


class TaskOutcome(str, Enum):
    VERIFIED = "VERIFIED"
    PARTIAL = "PARTIAL"
    BLOCKED = "BLOCKED"
    FAILED = "FAILED"
    UNKNOWN = "UNKNOWN"
    CANCELLED = "CANCELLED"


@dataclass(frozen=True)
class TaskSpec:
    objective: str
    origin: InputOrigin = InputOrigin.USER
    task_id: str = field(default_factory=lambda: uuid.uuid4().hex)
    constraints: tuple[str, ...] = ()
    authorized_scope: str = "existing_permissions_only"
    acceptance_criteria: tuple[dict[str, Any], ...] = ()
    parent_task_id: str | None = None

    def __post_init__(self):
        if not isinstance(self.objective, str) or not self.objective.strip():
            raise ValueError("A nonempty original objective is required")
        if not isinstance(self.origin, InputOrigin):
            raise TypeError("Origin must be a typed InputOrigin")
        if self.origin in (InputOrigin.TOOL, InputOrigin.WEB, InputOrigin.OCR, InputOrigin.SUBAGENT):
            raise ValueError("Observed content cannot create an authorized task")
        if not isinstance(self.task_id, str) or not self.task_id or len(self.task_id) > 128:
            raise ValueError("Invalid task id")
        if self.parent_task_id is not None and (not isinstance(self.parent_task_id, str)
                or not self.parent_task_id or len(self.parent_task_id) > 128 or self.parent_task_id == self.task_id):
            raise ValueError('Invalid parent task id')
        if not isinstance(self.constraints, tuple) or any(not isinstance(item, str) for item in self.constraints):
            raise ValueError('Invalid task constraints')
        if not isinstance(self.acceptance_criteria, tuple) or any(not isinstance(item, dict) for item in self.acceptance_criteria):
            raise ValueError('Acceptance criteria must be host-authored records')


@dataclass
class TaskState:
    status: str = "PLANNING"
    steps: int = 0
    tool_calls: int = 0
    reviews: int = 0
    replans: int = 0
    plan: dict[str, Any] = field(default_factory=dict)
    results: list[dict[str, Any]] = field(default_factory=list)
    metrics: list[dict[str, Any]] = field(default_factory=list)
    verification: dict[str, Any] = field(default_factory=dict)
    recovery_outcome: str = ''
    recovery_reason: str = ''
    recovery_read_only: bool = False
    recovery_decision_only: bool = False


@dataclass(frozen=True)
class WorkflowResult:
    task_id: str
    response: str
    outcome: TaskOutcome
    reason: str
    results: tuple[dict[str, Any], ...] = ()
    steps: int = 0
    retry_after_seconds: float | None = None

    @property
    def verified(self) -> bool:
        return self.outcome is TaskOutcome.VERIFIED
