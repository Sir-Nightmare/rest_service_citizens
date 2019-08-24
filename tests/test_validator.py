from copy import deepcopy

import pytest

from citizens_api.const import CITIZENS, RELATIVES
from citizens_api.validator import validate_import, validate_patch
from tests.const_for_test import BASE_IMPORT, CORRUPTIONS, PATCH_DICT

CITIZEN_PARAMETERS = BASE_IMPORT[CITIZENS][0]
PATCH_PARAMETERS = PATCH_DICT


def test_import_base_validation():
    assert validate_import(deepcopy(BASE_IMPORT))


@pytest.mark.parametrize("param", CITIZEN_PARAMETERS)
def test_import_not_all_params(param):
    payload = deepcopy(BASE_IMPORT)
    payload[CITIZENS][0].pop(param)
    with pytest.raises(AssertionError):
        validate_import(payload)


@pytest.mark.parametrize("param", CITIZEN_PARAMETERS)
def test_import_corrupted_params(param):
    for value in CORRUPTIONS[param]:
        payload = deepcopy(BASE_IMPORT)
        payload[CITIZENS][0][param] = value
        with pytest.raises(AssertionError):
            validate_import(payload)


def test_patch_base_validation():
    assert validate_patch(deepcopy(PATCH_DICT))


@pytest.mark.parametrize("param", ('town',))
def test_patch_one_param(param):
    assert validate_patch({param: PATCH_DICT[param]})


@pytest.mark.parametrize("param", [key for key in PATCH_DICT.keys() if key != RELATIVES])
def test_patch_corrupted_params(param):
    for value in CORRUPTIONS[param]:
        payload = deepcopy(PATCH_DICT)
        payload[param] = value
        with pytest.raises(AssertionError):
            validate_patch(payload)
