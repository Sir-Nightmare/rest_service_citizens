from datetime import datetime


class Validator:
    def validate_import(self, payload: dict) -> bool:
        citizen_dict = {}
        for person in payload["citizens"]:
            # TODO do we need to make a copy? depends on way to add to db
            id = person.pop("citizen_id")
            assert id not in citizen_dict, f"There's citizen id which is not unique: {id}"
            citizen_dict[id] = person
            try:
                datetime.strptime(person["birth_date"], "%d.%m.%Y")
            except ValueError:
                raise AssertionError(f"Date {person['birth_date']} is wrong or has wrong format")

        for citizen_id, properties in citizen_dict.items():
            for id in properties["relatives"]:
                try:
                    assert citizen_id in citizen_dict[id]["relatives"], "relative connection is wrong"
                except KeyError:
                    raise AssertionError(f"Id {id} of a relative does not exist in import")
        return True
