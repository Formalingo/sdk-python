from enum import Enum

class DocumentsPutRequestBody_status(str, Enum):
    Draft = "draft",
    Published = "published",
    Completed = "completed",
    Expired = "expired",

