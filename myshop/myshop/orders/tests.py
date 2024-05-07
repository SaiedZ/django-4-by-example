import pytest
from django.test import TestCase

from .forms import OrderCreateForm


@pytest.mark.parametrize(
    "first_name, last_name, email, address, postal_code, city, expected_is_valid",
    [
        # Happy path tests
        pytest.param("John", "Doe", "john.doe@example.com", "123 Elm Street",
                     "12345", "Springfield", True, id="all_valid_fields"),
        pytest.param("Jane", "Smith", "jane.smith@example.com", "456 Oak Avenue",
                     "67890", "Shelbyville", True, id="all_valid_fields_alternate"),

        # Edge cases
        pytest.param("J", "D", "j.d@example.com", "1 Elm Street",
                     "11111", "Smalltown", True, id="minimal_valid_fields"),

        # Error cases
        pytest.param("", "Doe", "john.doe@example.com", "123 Elm Street",
                     "12345", "Springfield", False, id="missing_first_name"),
        pytest.param("John", "", "john.doe@example.com", "123 Elm Street",
                     "12345", "Springfield", False, id="missing_last_name"),
        pytest.param("John", "Doe", "", "123 Elm Street", "12345",
                     "Springfield", False, id="missing_email"),
        pytest.param("John", "Doe", "john.doe@example.com", "",
                     "12345", "Springfield", False, id="missing_address"),
        pytest.param("John", "Doe", "john.doe@example.com", "123 Elm Street",
                     "", "Springfield", False, id="missing_postal_code"),
        pytest.param("John", "Doe", "john.doe@example.com",
                     "123 Elm Street", "12345", "", False, id="missing_city"),
    ]
)
def test_order_create_form_validation(
    first_name, last_name, email, address, postal_code, city, expected_is_valid
):
    form_data = {
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'address': address,
        'postal_code': postal_code,
        'city': city
    }
    form = OrderCreateForm(data=form_data)
    assert form.is_valid(
    ) is expected_is_valid, f"Expected form.is_valid() to be {expected_is_valid} but got {form.is_valid()}"

    assert bool(form.errors) is not expected_is_valid, "Form should have errors"
