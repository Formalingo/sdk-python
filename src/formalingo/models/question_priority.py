from enum import Enum

class Question_priority(str, Enum):
    Low = "low",
    Medium = "medium",
    High = "high",
    Critical = "critical",

