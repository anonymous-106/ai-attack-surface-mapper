from dataclasses import dataclass, field
from typing import Any

@dataclass
class ReconResult:
    module: str
    target: str
    success: bool
    data: Any = None
    error: str | None = None
    metadata: dict = field(default_factory=dict)

    