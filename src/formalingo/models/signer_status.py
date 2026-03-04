from enum import Enum

class Signer_status(str, Enum):
    Pending = "pending",
    Viewed = "viewed",
    Completed = "completed",

