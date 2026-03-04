from enum import Enum

class DocumentSubmission_status(str, Enum):
    Pending = "pending",
    In_progress = "in_progress",
    Completed = "completed",

