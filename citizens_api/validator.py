from datetime import datetime

import fastjsonschema
from fastjsonschema import JsonSchemaException

from citizens_api.const import SCHEMA_DICT, PATCH_SCHEMA, CITIZENS, CITIZEN_ID, BIRTH_DATE, RELATIVES


def validate_import(payload: dict) -> bool:
    validate = fastjsonschema.compile(SCHEMA_DICT)
    try:
        validate(payload)
    except JsonSchemaException:
        raise AssertionError("Import json doesn't meet the schema")

    citizen_dict = {}
    for person in payload[CITIZENS]:
        # TODO do we need to make a copy? depends on way to add to db
        try:
            citizen_id = person.pop(CITIZEN_ID)
        except KeyError:
            raise AssertionError("There's no key citizen_id")
        assert citizen_id not in citizen_dict, f"There's citizen id which is not unique: {citizen_id}"
        citizen_dict[citizen_id] = person
        try:
            datetime.strptime(person[BIRTH_DATE], "%d.%m.%Y")
        except ValueError:
            raise AssertionError(f"Date {person['birth_date']} is wrong or has wrong format")

    for citizen_id, properties in citizen_dict.items():
        for person_id in properties[RELATIVES]:
            try:
                assert citizen_id in citizen_dict[person_id][RELATIVES], "Relative connection is wrong"
            except KeyError:
                raise AssertionError(f"Id {person_id} of a relative does not exist in import")
    return True


def validate_patch(payload: dict) -> bool:
    validate = fastjsonschema.compile(PATCH_SCHEMA)
    try:
        validate(payload)
    except JsonSchemaException:
        raise AssertionError("Patch json doesn't meet the schema")
    if BIRTH_DATE in payload:
        try:
            datetime.strptime(payload[BIRTH_DATE], "%d.%m.%Y")
        except ValueError:
            raise AssertionError(f"Date {payload['birth_date']} is wrong or has wrong format")
    return True
