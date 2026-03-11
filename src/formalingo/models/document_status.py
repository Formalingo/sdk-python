from enum import Enum

class Document_status(str, Enum):
    Draft = "draft",
    Published = "published",
    Completed = "completed",
    Expired = "expired",

