from enum import Enum

class PhoneValidationError_details_code(str, Enum):
    Missing_default_country = "missing_default_country",
    Invalid_country = "invalid_country",
    Invalid_phone = "invalid_phone",

