from copy import deepcopy

import pytest

from citizens_api.validator import Validator
from tests.const import BASE_IMPORT, CORRUPTIONS

validator = Validator().validate_import
CITIZEN_PARAMETERS = BASE_IMPORT["citizens"][0]


def test_base_validation():
    assert validator(BASE_IMPORT)


@pytest.mark.parametrize("param", CITIZEN_PARAMETERS)
def test_not_all_params(param):
    payload = deepcopy(BASE_IMPORT)
    payload["citizens"][0].pop(param)
    assert validator(payload) is False


@pytest.mark.parametrize("param", CITIZEN_PARAMETERS)
def test_corrupted_params(param):
    for value in CORRUPTIONS[param]:
        payload = deepcopy(BASE_IMPORT)
        payload["citizens"][0][param] = value
        assert validator(payload) is False