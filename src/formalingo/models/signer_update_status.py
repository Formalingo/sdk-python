from enum import Enum

class SignerUpdate_status(str, Enum):
    Pending = "pending",
    Viewed = "viewed",
    Completed = "completed",

