from enum import Enum

class WithQPutRequestBody_priority(str, Enum):
    Low = "low",
    Medium = "medium",
    High = "high",
    Critical = "critical",

