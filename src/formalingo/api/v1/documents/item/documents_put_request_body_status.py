from enum import Enum

class DocumentsPutRequestBody_status(str, Enum):
    Draft = "draft",
    Sent = "sent",
    Completed = "completed",
    Expired = "expired",

