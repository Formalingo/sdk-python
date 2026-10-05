from enum import Enum

class RecipientCreateResult_status(str, Enum):
    Not_started = "not_started",
    In_progress = "in_progress",
    Completed = "completed",

