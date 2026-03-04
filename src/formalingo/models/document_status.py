from enum import Enum

class Document_status(str, Enum):
    Draft = "draft",
    Sent = "sent",
    Completed = "completed",
    Expired = "expired",

