from enum import Enum

class WithFPutRequestBody_type(str, Enum):
    Short_text = "short_text",
    Long_text = "long_text",
    Mcq = "mcq",
    Multi_select = "multi_select",
    Rating = "rating",
    Date = "date",
    Number = "number",
    Yes_no = "yes_no",
    File_upload = "file_upload",
    Dropdown = "dropdown",
    Digital_signature = "digital_signature",
    Email = "email",
    Phone = "phone",
    Initials = "initials",

