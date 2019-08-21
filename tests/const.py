BASE_IMPORT = {
    "citizens": [
        {
            "citizen_id": 1,
            "town": "Москва",
            "street": "Льва Толстого",
            "building": "16к7стр5",
            "apartment": 7,
            "name": "Иванов Иван Иванович",
            "birth_date": "26.12.1986",
            "gender": "male",
            "relatives": [2]
        },
        {
            "citizen_id": 2,
            "town": "Москва",
            "street": "Льва Толстого",
            "building": "16к7стр5",
            "apartment": 7,
            "name": "Иванов Сергей Иванович",
            "birth_date": "17.04.1997",
            "gender": "male",
            "relatives": [1]
        },
        {
            "citizen_id": 3,
            "town": "Керчь",
            "street": "Иосифа Бродского",
            "building": "2",
            "apartment": 11,
            "name": "Романова Мария Леонидовна",
            "birth_date": "23.11.1986",
            "gender": "female",
            "relatives": []
        }
    ]
}

CORRUPTIONS = {
    "citizen_id": (None, "", "&", 2),
    "town": (None, "", "&", 2),
    "street": (None, "", "&", 2),
    "building": (None, "", "&", 2),
    "apartment": (None, "", "&", 1.456),
    "name": (None, "", 2),
    "birth_date": (None, "", "&", "31.02.2019", "12.28.2019", "31.12.19", "31/12/2019", "2019.12.31"),
    "gender": (None, "", "&", 1, "agender"),
    "relatives": (None, "", "&", [3], [2, 2])
}

PATCH_DICT = {
    "town": "Москва",
    "street": "Льва Толстого",
    "building": "16к7стр5",
    "apartment": 7,
    "name": "Иванова Мария Леонидовна",
    "birth_date": "26.12.1986",
    "gender": "male",
    "relatives": [1]
}
PROPERTIES_DICT = {"citizen_id": {"type": "integer"},
                   "town": {"type": "string"},
                   "street": {"type": "string"},
                   "building": {"type": "string"},
                   "apartment": {"type": "integer"},
                   "name": {"type": "string"},
                   "birth_date": {"type": "string", "pattern": r"^([0123][0-9]).([012][0-9]).(\d{4})$"},
                   "gender": {"type": "string", "enum": ["male", "female"]},
                   "relatives": {"type": "array", "uniqueItems": True, "items": {"type": "integer"}}}

SCHEMA_DICT = {
    "type": "object",
    "properties": {
        "citizens": {"type": "array", "minItems": 1, "items": {"type": "object", "properties": PROPERTIES_DICT}},
    }
}

import fastjsonschema

validate = fastjsonschema.compile(SCHEMA_DICT)
print(validate(BASE_IMPORT))
