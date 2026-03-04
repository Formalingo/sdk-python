from enum import Enum

class GetStatusQueryParameterType(str, Enum):
    Draft = "draft",
    Sent = "sent",
    Completed = "completed",
    Expired = "expired",

