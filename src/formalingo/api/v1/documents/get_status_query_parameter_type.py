from enum import Enum

class GetStatusQueryParameterType(str, Enum):
    Draft = "draft",
    Published = "published",
    Completed = "completed",
    Expired = "expired",

