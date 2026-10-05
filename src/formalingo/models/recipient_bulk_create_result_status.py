from enum import Enum

class RecipientBulkCreateResult_status(str, Enum):
    Not_started = "not_started",
    In_progress = "in_progress",
    Completed = "completed",

