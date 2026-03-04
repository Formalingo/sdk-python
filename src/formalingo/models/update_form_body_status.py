from enum import Enum

class UpdateFormBody_status(str, Enum):
    Draft = "draft",
    Published = "published",
    Archived = "archived",

