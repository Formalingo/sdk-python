from enum import Enum

class StartDocumentParseJobResponse_data_status(str, Enum):
    Pending = "pending",
    Processing = "processing",
    Completed = "completed",
    Failed = "failed",

