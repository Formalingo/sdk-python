from enum import Enum

class CreateQuestionBody_priority(str, Enum):
    Low = "low",
    Medium = "medium",
    High = "high",
    Critical = "critical",

