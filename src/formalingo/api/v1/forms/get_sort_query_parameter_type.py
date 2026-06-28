from enum import Enum

class GetSortQueryParameterType(str, Enum):
    Updated = "updated",
    Created = "created",
    Submissions = "submissions",
    Sent = "sent",
    Title = "title",

