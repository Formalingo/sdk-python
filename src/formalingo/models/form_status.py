from enum import Enum

class Form_status(str, Enum):
    Draft = "draft",
    Published = "published",
    Archived = "archived",

