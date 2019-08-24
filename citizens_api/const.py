DEFAULT_HOST = "0.0.0.0"
DEFAULT_PORT = 8080

CITIZENS, CITIZEN_ID, TOWN, STREET, BUILDING, APARTMENT, NAME, BIRTH_DATE, GENDER, RELATIVES = (
    "citizens", "citizen_id", "town", "street", "building", "apartment", "name", "birth_date", "gender", "relatives")

PROPERTIES_DICT = {
    CITIZEN_ID: {"type": "integer"},
    TOWN: {"type": "string", "pattern": r"\w+"},
    STREET: {"type": "string", "pattern": r"\w+"},
    BUILDING: {"type": "string", "pattern": r"\w+"},
    APARTMENT: {"type": "integer"},
    NAME: {"type": "string", "minLength": 1},
    BIRTH_DATE: {"type": "string", "pattern": r"^([0123]?\d{1}).([012]?\d{1}).(\d{4})$"},
    GENDER: {"type": "string", "enum": ["male", "female"]},
    RELATIVES: {"type": "array", "uniqueItems": True, "items": {"type": "integer"}}
}

PATCH_SCHEMA = {
    "type": "object",
    "properties": {k: v for k, v in PROPERTIES_DICT.items() if k != CITIZEN_ID},
    "additionalProperties": False,
    "minProperties": 1
}

SCHEMA_DICT = {
    "type": "object",
    "properties": {
        CITIZENS: {
            "type": "array", "minItems": 1, "items": {"type": "object",
                                                      "properties": PROPERTIES_DICT,
                                                      "additionalProperties": False,
                                                      "required": list(PROPERTIES_DICT.keys())}
        }

    },
    "required": [CITIZENS]
}

print(PATCH_SCHEMA)
