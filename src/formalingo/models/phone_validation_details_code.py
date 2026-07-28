from enum import Enum

class PhoneValidationDetails_code(str, Enum):
    Missing_default_country = "missing_default_country",
    Invalid_country = "invalid_country",
    Invalid_phone = "invalid_phone",

